import os
import json
from web3 import Web3
from pathlib import Path
import streamlit as st
from openai import OpenAI
import requests

from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json


# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

############## DALLE 3 ##########################

# Initialize OpenAI client with API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

generated_image_url = None  # Declare it globally to hold the generated image data

def generate_image(img_description):
    global generated_image_url
    img_response = client.images.generate(
            model="dall-e-3",
            prompt=img_description,
            size="1024x1024",
            quality="standard",
            n=1  # Always generate only one image
    )
    generated_image_url = img_response.data[0].url
    # Download the image data from the URL

st.subheader("POWERED BY OPENAI & PINATA!!!!")
img_description = st.text_input("Enter a description for the image you want to generate:")

# Create a button to generate images
if st.button("Generate Image") and img_description:
    with st.spinner(text='Generating image...'):
        generate_image(img_description)
        st.image(generated_image_url)

################################################################################
# Load_Contract Function
################################################################################


@st.cache_resource
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/artregistry_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()

################################################################################
# Helper functions to pin files and json to Pinata
################################################################################

def pin_artwork(artwork_name, artwork_url):
    # Pin the file to IPFS with Pinata
    ipfs_file_hash = pin_file_to_ipfs(requests.get(artwork_url).content)

    # Build a token metadata file for the artwork
    token_json = {
        "name": artwork_name,
        "image": ipfs_file_hash
    }
    json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
    json_ipfs_hash = pin_json_to_ipfs(json_data)

    return json_ipfs_hash, token_json

st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

################################################################################
# Register New Artwork
################################################################################
st.markdown("## Register New Artwork")
artwork_name = st.text_input("Enter the name of the artwork")
artist_name = st.text_input("Enter the artist name")

# Grabs the URL's image & send it to Pinata.
file = generated_image_url

if st.button("Register Artwork"):
    # Step 1: Pin the artwork to IPFS and get the IPFS hash
    artwork_ipfs_hash, token_json = pin_artwork(artwork_name, generated_image_url)

    artwork_uri = f"ipfs://{artwork_ipfs_hash}"

    # Step 2: Register the artwork on the blockchain
    tx_hash = contract.functions.registerArtwork(
        address,
        artwork_name,
        artist_name,
        artwork_uri,
        token_json['image']
    ).transact({'from': address, 'gas': 1000000})
    
    # Step 3: Wait for the transaction to be mined and get the receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    # Display transaction receipt and IPFS links
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    st.write("You can view the pinned metadata file with the following IPFS Gateway Link")
    st.markdown(f"[Artwork IPFS Gateway Link](https://ipfs.io/ipfs/{artwork_ipfs_hash})")
    st.markdown(f"[Artwork IPFS Image Link](https://ipfs.io/ipfs/{token_json['image']})")

st.markdown("---")
st.write(generated_image_url) # Test to see if the image url is generated

# NOTE:
# For some reason, the generated image keeps resetting giving a blank url.
import os
import json
from web3 import Web3
from pathlib import Path
import streamlit as st
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

#################################################

json_headers = {
    "Content-Type": "application/json",
    "PINATA_API_KEY": os.getenv("PINATA_API_KEY"),
    "PINATA_SECRET_API_KEY": os.getenv("PINATA_SECRET_API_KEY"),
}

file_headers = {
    "PINATA_API_KEY": os.getenv("PINATA_API_KEY"),
    "PINATA_SECRET_API_KEY": os.getenv("PINATA_SECRET_API_KEY"),
}

def convert_data_to_json(content):
    data = {"pinataOptions": {"cidVersion": 1}, "pinataContent": content}
    return json.dumps(data)

def pin_file_to_ipfs(data):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinFileToIPFS",
        files={'file': data},
        headers=file_headers
    )
    print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash

def pin_json_to_ipfs(json):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinJSONToIPFS",
        data=json,
        headers=json_headers
    )
    print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash
################################################

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

############## DALLE 3 ##########################

# Initialize OpenAI client with API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

generated_image_url = None  # Declare it globally to hold the generated image data

def generate_image(img_description):
    global generated_image_url
    try:
        img_response = client.images.generate(
            model="dall-e-3",
            prompt=img_description,
            size="1024x1024",
            quality="standard",
            n=1  # Always generate only one image
        )
        generated_image_url = img_response.data[0].url
        # st.write("Generated Image URL:", generated_image_url)  # For Debugging Purposes
    except Exception as e:
        st.error(f"Error generating image: {e}")

st.subheader("POWERED BY OPENAI & PINATA!!!!")
img_description = st.text_input("Enter a description for the image you want to generate:")

# Initialize session state
if 'image_content' not in st.session_state:
    st.session_state.image_content = None
if 'artwork_url' not in st.session_state:
    st.session_state.artwork_url = None

# Create a button to generate images
if st.button("Generate Image") and img_description:
    with st.spinner(text='Generating image...'):
        generate_image(img_description)
        
        # Fetch the image from the URL
        response = requests.get(generated_image_url)
        
        # Open the image
        image_content = Image.open(BytesIO(response.content))
        
        # Update session state with the new image content
        st.session_state.image_content = image_content

        # Save the generated image URL to session state
        st.session_state.artwork_url = generated_image_url
        
# Display the image
if st.session_state.image_content is not None:
    st.image(st.session_state.image_content, use_column_width=True)

################################################################################
# Load_Contract Function
################################################################################

@st.cache_resource
def load_contract():

    # Load the contract ABI
    with open(Path('/home/jiaoyinyang/Documents/UMN_FinTech/UofM-VIRT-FIN-PT-11-2023-U-LOLC-main/01-Sessions/22-dApps/2/Activities/06-Evr_Art_Registry_with_IPFS/Solved/ArtRegistry/NFT_APP/pages/NFT_Minter_files/contracts/compiled/nft_registry_abi.json')) as f:
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
        "address": address,
        "artwork_name": artwork_name,
        "artist_name": artist_name,
        "message": message,
        "prompt": img_description,
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
message = st.text_area("Message:", height=100)

# Load image_content from session state
image_content = st.session_state.image_content

# Load artwork_url from session state
artwork_url = st.session_state.artwork_url

if st.button("Register Artwork") and image_content and artwork_url:
    # Step 1: Pin the artwork to IPFS and get the IPFS hash
    artwork_ipfs_hash, token_json = pin_artwork(artwork_name, artwork_url)

    artwork_uri = f"ipfs://{artwork_ipfs_hash}"
    st.write(artwork_uri)
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
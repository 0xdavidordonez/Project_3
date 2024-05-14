import streamlit as st
from openai import OpenAI
from PIL import Image                                       
import json
import requests
from streamlit_lottie import st_lottie
import base64

# Set page title and description
st.set_page_config(page_title="Block Magic NFT Collection")

# Display the main header centered with HTML
st.markdown("<h1 style='text-align: center;'>Block Magic NFT Collection</h1>", unsafe_allow_html=True)

# Display the subheader centered with HTML
st.markdown("<h2 style='text-align: center;'>Dynamic, Evolving Artwork on the Blockchain</h2>", unsafe_allow_html=True)

st.markdown("")
st.markdown("")
st.markdown("")

# Display the main header
st.header("Block Magic NFT Collection")

# Display the subheader
st.subheader("Dynamic, Evolving Artwork on the Blockchain")

# Markdown for detailed description
st.markdown("""
Welcome to the **Block Magic NFT Collection**, a unique series of digital collectibles that evolve over time on the Ethereum blockchain. Each NFT starts as a 'Loot Box' and evolves into a piece of artwork, providing a dynamic and interactive experience for collectors.

**Features:**
- **Dynamic Evolution:** Each NFT can evolve from a Loot Box to a piece of artwork based on interval updates using smart contract automation with ChainLink.
- **Blockchain Integrated:** Leveraging the Ethereum network for secure and verifiable ownership.
**Evolving Legacy:** Witness the transformation and legacy of your NFTs as they gain maturity and value over time.

""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

# Display a subheader
st.subheader("How it works:")
# Create three columns
col1, col2, col3 = st.columns([12, 10, 10])

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_0 = load_lottiefile("lottiefiles/Animation - 1714928906685.json")
lottie_hello0 = load_lottieurl("https://lottie.host/ebc469d4-b369-4b6a-b3e3-17480524f172/OKlNtrTeOx.json")

with col1:
    st_lottie(
        lottie_hello0,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height="250px",
        width="200px",
        key=None,
    )
    st.caption('Connect your wallet to OpenSea')
######################
lottie_coding2 = load_lottiefile("lottiefiles/Animation - 1714929179608.json")
lottie_hello2 = load_lottieurl("https://lottie.host/f1e45f7e-0e6b-40b6-85fd-92917eef0eeb/rnpUOaFSl3.json")

with col2:
    st_lottie(
        lottie_hello2,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height="200px",
        width="200px",
        key=None,
    )
    st.caption('Purchase a mistery box')
#########################
lottie_coding3 = load_lottiefile("lottiefiles/Animation - 1714929215195.json")
lottie_hello3 = load_lottieurl("https://lottie.host/7227b19d-8b5f-4f40-b519-4086486a4e65/gxARNDD1AS.json")

with col3:
    st_lottie(
        lottie_hello3,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height="250px",
        width="200px",
        key=None,
    )
    st.caption('Watch your Minted NFT creation evolve!')

st.markdown("")
st.markdown("")
st.markdown("")
# HTML and JavaScript to create a centered button that opens a URL
url = "https://testnets.opensea.io/collection/block-magic-nft-collection-7"
button_html = f"""
<div style="text-align: center;">
    <a href="{url}" target="_blank" rel="noopener noreferrer">
        <button style='color: black; background-color: #FF4B4B; padding: 10px 24px; font-size: 18px; border: none; cursor: pointer;'>
            View Collection on OpenSea
        </button>
    </a>
</div>
"""
st.markdown(button_html, unsafe_allow_html=True)
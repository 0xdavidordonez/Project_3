from openai import OpenAI
from PIL import Image
import streamlit as st                                         
import json
import requests
from streamlit_lottie import st_lottie
import base64

# Initialize OpenAI client with API key and streamlit page config
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Arcane Cypher: Next Generation NFTs", page_icon=":robot_face:", layout="wide",
                  initial_sidebar_state="collapsed")
###############################################
#title config

st.markdown(
    """
    <h1 class="title">ARCANE CYPHER</h1>
    """,
    unsafe_allow_html=True
)

# CSS for the title
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-family: ;
        color: #FF5733;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#sidebar styling ################################
st.sidebar.header("Select Page")

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image1.jpg")

page_bg_img = f"""
<style>
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
###################################################

def generate_images(img_description):
    img_response = client.images.generate(
        model="dall-e-3",
        prompt=img_description,
        size="1024x1024",
        quality="high",
        n=1 
    )
    image_url = img_response.data[0].url
    return image_url

######################################################

##lottie animation # 1
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding1 = load_lottiefile("lottiefiles/Animation - 1714978434402 (1).json")  
lottie_bg1 = load_lottieurl("https://lottie.host/ce879bc5-2e04-4233-909b-e51d34f36298/mn0BN7Rhtm.json")

# Display the background Lottie animation
st_lottie(
    lottie_bg1,
    speed=0.5,
    reverse=False,
    loop=True,
    quality="high",
    height="110%",
    width="100%",
    key="background",
)

# Center the title
st.markdown('<h1 class="title">NFT Generator Tool &#x1F9D9;</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subheader">Powered by Blockchain</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap');
    /* Custom styles for title */
    .title {
        font-family: 'Roboto', sans-serif;
        text-align: center;
        font-size: 50px;  /* Adjust the size as needed */
    }
    /* Custom styles for subheader */
    .subheader {
        font-family: 'Montserrat', sans-serif;
        color: #4a90e2;
        text-align: center;
        font-size: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Adding more vertical space
st.markdown("#")
st.markdown("#")
st.markdown("#")

#####################################################################################################################
col1, col2 = st.columns([10, 5])
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("lottiefiles/Animation - 1714929179608.json")
lottie_hello = load_lottieurl("https://lottie.host/f1e45f7e-0e6b-40b6-85fd-92917eef0eeb/rnpUOaFSl3.json")

with col1:
    st.write("Arcane Cypher is a cutting-edge dApp leveraging artificial intelligence to create unique, AI-generated NFTs tokenized on the Ethereum blockchain. This innovative platform not only allows users to generate one-of-a-kind NFT artworks based on their input but also features a dynamic NFT marketplace. Here, users can explore and purchase 'loot boxes,' which evolve into distinctive NFT art upon minting. These evolving NFTs offer a novel and interactive way for collectors and enthusiasts to engage with digital art. All NFTs created and purchased through Arcane Cypher can be seamlessly traded on OpenSea, enabling easy access to a broader marketplace and community. Arcane Cypher is your gateway to exploring and owning evolving digital art in this blockchain era.")

with col2:
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height="250px",
        width="350px",
        key=None,
    )
########################################


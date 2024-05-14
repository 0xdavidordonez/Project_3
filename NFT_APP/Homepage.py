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
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Covered+By+Your+Grace&display=swap');
    .title {
        text-align: center;
        font-family: ;
        color: #FF5733;
        font-family: 'Covered By Your Grace', cursive;
        font-size: 80px;
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

# Center the headers
st.markdown(
    '''
    <h2 class="header" style="text-align: center;">AI art and NFTs finally meet &#x1F9D9;</h2>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
    <h2 class="subheader" style="font-family: 'Monospace'; color: DarkTurquoise; text-align: center; ">Powered by the Ethereum Blockchain</h2>
    ''',
    unsafe_allow_html=True
)




# Adding more vertical space
st.markdown("#")
st.markdown("#")
st.markdown("#")

#####################################################################################################################
col1, col2 = st.columns([10, 5])

    

lottie_coding1 = load_lottiefile("lottiefiles/Animation - 1714928235124.json")
lottie_hello1 = load_lottieurl("https://lottie.host/df35c1fb-86a9-4d07-bf09-3a53058ae686/JVJmZz3k3i.json")


with col1:
    st.markdown(
    '''
    <div style="font-family: 'Monospace';">
        <p> Unveil the frontier of digital creativity with our pioneering decentralized application (dApp). Built on the robust Ethereum blockchain, <strong>Arcane Cypher</strong> harnesses the power of artificial intelligence to craft exclusive, AI-generated NFTs. This platform revolutionizes the NFT landscape by empowering you to create personalized NFT artworks and tokenizing them.</p>
        <p>Discover our dynamic NFT marketplace, where you can acquire transformative 'Loot Boxes'. These boxes evolve into unique NFT art pieces when minted, offering an engaging and innovative experience for digital art collectors and enthusiasts alike. Each NFT you create or acquire on <strong>Arcane Cypher</strong> can be effortlessly traded on OpenSea, providing you with seamless integration into an expansive network of collectors and digital markets. Step into the future of digital art ownership and interaction with <strong>Arcane Cypher</strong>, your portal to the evolving world of blockchain-based art.</p>
    </div>
    ''',
    unsafe_allow_html=True
)

with col2:
    st_lottie(
        lottie_hello1,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height="200px",
        width="300px",
        key=None,
    )
########################################

#contract adresses
st.markdown("#")
st.markdown("#")


# Markdown for NFT Minter Address
st.markdown(
    '''
    <div style="font-family: 'Monospace';">
        <p><strong style="font-size: 25px;">NFT Minter Address:</strong></p>
        <p>0xf702F132F5110f0dFe785A794B09760e684c23EC</p> 
    </div>
    ''',
    unsafe_allow_html=True
)

# Markdown for Dynamic NFT Address
st.markdown(
    '''
    <div style="font-family: 'Monospace';">
        <p><strong style="font-size: 25px;">Dynamic NFT Address:</strong></p>
        <p>0x567fc97EBaFD150457661cDF8C440dAcdfd0fF5D</p>  
    </div>
    ''',
    unsafe_allow_html=True
)
###############################################
st.markdown("#")
st.markdown("#")

# Big header that transitions into the next area
st.markdown(
    '''
    <div style="font-family: 'Monospace'; text-align: center;">
        <h1 style="font-size: 65px;">Create with AI Art Generator: Bring your Ideas to Reality</h1>
    </div>
    ''',
    unsafe_allow_html=True
)

st.image('dragon.jpg')

st.markdown("#")
st.markdown("#")
#description and link to ourNFT minter app

st.markdown(
    '''
    <div style="font-family: 'Roboto';">
        <h1>Discover the Art of Possibility with Our AI-Powered NFT Minter</h1>
        <p>Empowering artists and innovators, our platform harnesses the power of <strong>Generative Artificial Intelligence (AI)</strong> to turn imaginative text prompts into ethereal visual artworks. This cutting-edge technology allows users to generate detailed and unique images, bringing abstract concepts to vivid life.</p>
        <p>Once your creation is complete, our NFT minter tool takes over. It automatically tokenizes the generated images, ensuring each piece is securely registered on the blockchain. This seamless integration into the digital ledger not only protects the authenticity of your artwork but also simplifies the process of entering the NFT market.</p>
        
    </div>
    ''',
    unsafe_allow_html=True
)


st.markdown(
    '''
    <div style="display: flex; justify-content: center; align-items: center;">
        <a href="pages/NFT_Minter.py" target="_self">
            <button style="color: white; background-color: blue; border: none; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;">
                Go to NFT Minter APP
            </button>
        </a>
    </div>
    ''',
    unsafe_allow_html=True
)


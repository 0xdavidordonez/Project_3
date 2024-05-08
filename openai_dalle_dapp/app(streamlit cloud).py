from openai import OpenAI
from PIL import Image
import streamlit as st 


# Initialize OpenAI client with API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_images(img_description):
    img_response=client.images.generate(
            model="dall-e-3",
            prompt=img_description,
            size="1024x1024",
            quality="standard",
            n=1  # Always generate only one image
        
    )
    image_url = img_response.data[0].url
    return image_url
st.set_page_config(page_title="DALL-E-3 Image Generation", page_icon=":camera:", layout="wide")

# Create a title
st.title("DALL-E-3 Image Generation Tool")

st.subheader("POWERED BY OPENAI!!!!")
img_description = st.text_input("Enter a description for the image you want to generate:")

# Create a button to generate images
if st.button("Generate Image") and img_description:
    with st.spinner(text='Generating image...'):
        generate_image=generate_images(img_description)
        st.image(generate_image)
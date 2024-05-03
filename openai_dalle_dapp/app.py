import OpenAI
from PIL import Image
import streamlit as st
import os                                          # Needed for dotenv
from dotenv import load_dotenv                     # To load key.env correctly

# Load environment variables from key.env file
load_dotenv("key.env")

# Retrieve API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if the API key is properly loaded
if OPENAI_API_KEY is None:
    raise ValueError("OpenAI API key is not provided. Please check your key.env file.")

# Initialize OpenAI client with API key
client = openai.Client(api_key=OPENAI_API_KEY)

def generate_image(image_description):
    try:
        img_response = client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size="1024x1024",
            quality="standard",
            n=1  # Always generate only one image
        )
        image_url = img_response.data[0].url
        return image_url
    except Exception as e:
        st.error(f"Error generating image: {e}")

st.set_page_config(page_title="DALL-E-3 Image Generation", page_icon=":camera:", layout="wide")

# Create a title
st.title("DALL-E-3 Image Generation Tool")

st.subheader("POWERED BY OPENAI!!!!")
img_description = st.text_input("Enter a description for the image you want to generate:")

# Create a button to generate images
if st.button("Generate Image") and img_description:
    generated_image_url = generate_image(img_description)
    st.image(generated_image_url)

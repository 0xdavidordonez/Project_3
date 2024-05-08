import openai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("OPENAI_API_KEY")
client = openai.Client(api_key=apikey)

def generate_image(description):
    response = client.images.generate(
        model="dall-e-3",
        prompt=description,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return [img_data.url for img_data in response.data]

st.set_page_config(page_title="DALL-E-3 Image Generation", page_icon=":camera:", layout="wide")
st.title("DALL-E-3 Image Generation Tool")

description = st.text_input("Enter image description:")
if st.button("Generate Image"):
    image_urls = generate_image(description)
    for url in image_urls:
        st.image(url)

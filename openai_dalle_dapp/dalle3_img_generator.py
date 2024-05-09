from openai import OpenAI
import streamlit as st
from pinata_upload import upload_image_to_pinata as upload

# Initialize OpenAI client with API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

generated_image_url = None  # Declare it globally to hold the generated image URL

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

st.set_page_config(page_title="DALL-E-3 Image Generation", page_icon=":camera:", layout="wide")

# Create a title
st.title("DALL-E-3 Image Generation Tool")

st.subheader("POWERED BY OPENAI!!!!")
img_description = st.text_input("Enter a description for the image you want to generate:")

# Create a button to generate images
if st.button("Generate Image") and img_description:
    with st.spinner(text='Generating image...'):
        generate_image(img_description)
        st.image(generated_image_url)

# Print the URL of the generated image outside the button click
if generated_image_url:
    st.write("URL of the generated image:", generated_image_url)

########## PINATA ###########
upload(generated_image_url)

######### SmartContract - ArtRegistry Form ################


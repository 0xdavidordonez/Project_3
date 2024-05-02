import streamlit as st
import requests

# URL of the PNG image
image_url = 'https://cdn.discordapp.com/attachments/1039580033821446245/1233311624702459967/generated_image.png?ex=662fee35&is=662e9cb5&hm=8ebc4a2397c4033e32707c5d182da141fbe391a2699d324af06635dd639d81fe&'

# Fetch the image from the URL
response = requests.get(image_url)

# Display the image
st.image(response.content, caption='Generated Image', use_column_width=True)

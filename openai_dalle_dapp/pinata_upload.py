import requests
from datetime import datetime
import random

# Define your Pinata API key and secret
api_key = 'f7303b3c5de98f4f600d'
api_secret = '97ae5106d254e4878460552b2b69a07a8ce5af62cb778ea44a1ee1190ed79c85'

# Define the endpoint for Pinata's file pinning API
pinata_url = 'https://api.pinata.cloud/pinning/pinFileToIPFS'

# Define the image URL (generated from the ai)
# This variable needs to interact with the dapp. [haven't yet programmed]
image_url = 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-N2903MCX4oi2dA4wcnHstPDL/user-QRAeR5pWh9nAhuqYgvk1i5lr/img-1xys6rp2qCM1rmr8zicAyO28.png?st=2024-05-05T05%3A46%3A09Z&se=2024-05-05T07%3A46%3A09Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-05-04T21%3A37%3A22Z&ske=2024-05-05T21%3A37%3A22Z&sks=b&skv=2021-08-06&sig=HplNjchBpvo6gh2mAI7/MAki8VdfGbRKBWVFJ2/ySJY%3D'

# Generate a file name based on current date and time (short format) and a random number between 1 and 100
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
random_number = random.randint(1, 100)
file_name = f"image_{current_time}_{random_number}.jpg"

# Download the image from the URL
image_response = requests.get(image_url)

# Check if the image was downloaded successfully
if image_response.status_code == 200:
    # Prepare the request headers with your API key and secret
    headers = {
        'pinata_api_key': api_key,
        'pinata_secret_api_key': api_secret
    }

    # Prepare the request payload with the file data
    files = {
        'file': (file_name, image_response.content)
    }

    # Make the POST request to upload the file to Pinata
    response = requests.post(pinata_url, files=files, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response JSON, which contains the IPFS hash of the pinned file
        print("File uploaded successfully.\n\nIPFS hash:\n"+ response.json()['IpfsHash'])
    else:
        # Print the error message if the request failed
        print("Error uploading file:", response.text)
else:
    print("Failed to download image from the URL")

import streamlit as st
import requests # use for AI Image Generator & Reader
import json # used for reader
import time

# Need to update this every so often whenever you're going to use dapp
discord_token = "MzExOTQ1MDM2MDYzNTcxOTY5.GTrmtG.zcY3Yq0sWMmKRAlbDDdLj3cxJhDoi3zAOnlYOI"

####################### AI Image Generator ##################################################


def send_interaction(imagine_string):
    url = "https://discord.com/api/v9/interactions"

    payload = {
        "type": 2,
        "application_id": "1051209066925531206",
        "guild_id": "1039241590092353596",
        "channel_id": "1039580033821446245",
        "session_id": "a7bffccc363fdd844351a4168f83c8a0",
        "data": {
            "version": "1209945800017190929",
            "id": "1209945800017190925",
            "name": "imagine",
            "type": 1,
            "options": [
                {
                    "type": 3,
                    "name": "message",
                    "value": imagine_string
                }
            ],
            "application_command": {
                "id": "1209945800017190925",
                "type": 1,
                "application_id": "1051209066925531206",
                "version": "1209945800017190929",
                "name": "imagine",
                "description": "Generate Image with ReplyTensor",
                "options": [
                    {
                        "type": 3,
                        "name": "message",
                        "description": "No description provided",
                        "required": True,
                        "autocomplete": False,
                        "description_localized": "No description provided",
                        "name_localized": "message"
                    }
                ],
                "dm_permission": True,
                "integration_types": [0],
                "global_popularity_rank": 1,
                "description_localized": "Generate Image with ReplyTensor",
                "name_localized": "imagine"
            },
        }
    }

    headers = {
        "Authorization": discord_token
    }

    res = requests.post(url, json=payload, headers=headers)
    return res
    
# Example usage:
#imagine_string = "Bull vs Bear"

####################### STREAMLIT ##################################################

# Title of the web app
st.title("Evolving NFT AI Generator")

# Create a text input box
imagine_string = st.text_input("You generated an AI NFT:")

# Create a button
submitted = st.button("Submit")

# Check if the button is clicked
if submitted:
    # Display the input string
    # st.write("You entered:")
    
    response = send_interaction(imagine_string) # From The Image Generator
    print(response.text)

###################### Read Information From Discord ##################################################

# imagine_string = "Pig"

def retrieve_messages(channelid, imagine_string):
    headers = {
        "Authorization": discord_token
    }
    r = requests.get(f"https://discord.com/api/v9/channels/{channelid}/messages", headers=headers)
    jsonn = json.loads(r.text)

    # Sort messages by timestamp in descending order
    sorted_messages = sorted(jsonn, key=lambda x: x['timestamp'], reverse=True)

    for message in sorted_messages:
        if imagine_string in message.get('content', ''): 
            attachments = message.get('attachments', [])
            if attachments:
                return attachments[0]['url']

def retrieve_url():
    image_url = retrieve_messages('1039580033821446245', imagine_string)
    
    # Fetch the image from the URL
    response = requests.get(image_url)
    
    st.image(response.content, caption='Generated Image', use_column_width=True)

def loading():
    # Display the initial loading message
    loading_message = st.empty()
    loading_message.text("Loading... 60 seconds remaining")

    # Simulate loading for 60 seconds
    for i in range(60, 0, -1):
        loading_message.text(f"Loading... {i} seconds remaining")
        time.sleep(1)

    st.success("LOADING COMPLETED!!!")

if submitted:
    # Example usage
    loading()  # Assuming you want to simulate loading first
    retrieve_url()  # Then retrieve and display the image
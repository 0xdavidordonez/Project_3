import streamlit as st 
# Custom CSS to put iframe in the top right
# Create three columns
col1, col2, col3 = st.columns([1, 1, 2])  # Adjust the ratios as needed

# Use the last column to place the iframe
with col3:
    st.markdown(
        '<iframe scrolling="no" src="http://localhost:3000" width="700" height="500"></iframe>',
        unsafe_allow_html=True
    )

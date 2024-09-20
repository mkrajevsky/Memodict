import streamlit as st
from setup import Prompter

    # Function to send queries to GPT
def query_gpt(prompt):
        
        prompter = Prompter()
        response = prompter.query_gpt(prompt=prompt)
        return response   

    # Streamlit page configuration
st.set_page_config(page_title="Memodict", layout="wide")

with st.sidebar:
    st.title("GPT powered query interface")
    user_input = st.text_area("What would you like to be explaied:")
    user_multimodal_input = st.file_uploader("Upload an image or video", type=["jpg", "jpeg", "png", "mp4", "mov", "avi"])

# Main area
st.header("Memodict")
st.image("LOGO_MEMODICT.jpg", width=100)


if user_input:
    with st.spinner('Generating response...'):
        output = query_gpt(user_input)
        st.text_area("GPT's Response:", value=output, height=300)

    # Rating system
    st.header("Rate the Response")
    rating = st.slider("How do you rate the response from 1 to 5?", 1, 5, 1)
    if st.button('Submit Rating'):
        st.success(f"Thanks for your rating: {rating}/5")
        
if user_multimodal_input:
    st.image(user_multimodal_input, width=300)
    st.write("Multimodal input detected!")

# Run the Streamlit app by navigating to the folder containing the app.py file and running:
# streamlit run app.py


import streamlit as st
from PIL import Image

# st.set_page_config(layout="wide")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Open Camera"):
    camera_image = st.camera_input("Take a Photo")
# print(camera_image)

if camera_image:
    image = Image.open(camera_image)
    gray_image = image.convert("L")
    st.image(gray_image)

if uploaded_image:
    image = Image.open(uploaded_image)
    gray_image = image.convert("L")
    st.image(gray_image)






import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
import random
import streamlit as st
from PIL import Image

# Load the pre-trained style transfer model from TensorFlow Hub
hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
hub_module = hub.load(hub_handle)

# Function to load the style image for the selected style
def load_style_image(style_name, style_folder='art_styles', image_size=(256, 256)):
    style_image_path = os.path.join(style_folder, style_name, 'style_image.jpg')  # Ensure this is your style image name
    img = Image.open(style_image_path)
    img = img.resize(image_size)
    img = np.array(img)/255.0  # Normalize to [0, 1]
    img = np.expand_dims(img, axis=0)
    return img.astype(np.float32)  # Ensure the image is in float32 format

# Function to apply style transfer using TensorFlow Hub model
def apply_style_transfer(content_image, style_image):
    # Apply style transfer using the pre-trained model
    stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]
    return stylized_image

# Function to load the available styles from the dataset folder
def load_style_images(style_folder='art_styles'):
    style_images = {}
    for style_name in os.listdir(style_folder):
        style_path = os.path.join(style_folder, style_name)
        if os.path.isdir(style_path):
            style_images[style_name] = style_path  # Store folder path for style
    return style_images

# Function to load the content image
def load_image(uploaded_file):
    img = Image.open(uploaded_file)
    img = np.array(img)/255.0  # Normalize to [0, 1]
    img = np.expand_dims(img, axis=0)
    return img.astype(np.float32)  # Ensure the image is in float32 format

# Convert EagerTensor to PIL Image for Streamlit compatibility
def tensor_to_pil(tensor):
    tensor = tensor.numpy()
    tensor = np.squeeze(tensor, axis=0)  # Remove batch dimension
    tensor = np.clip(tensor, 0.0, 1.0)  # Ensure pixel values are in [0, 1]
    return Image.fromarray((tensor * 255).astype(np.uint8))

# Streamlit Interface
st.set_page_config(layout="wide")
st.title('Art Style Transfer')
st.markdown('Upload your image and choose a style from the dropdown.')

# Add a bit of styling
st.markdown("""
    <style>
    .main {
        max-width: 900px;
        margin: 0 auto;
        padding: 10px;
    }
    .stImage {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Layout improvements: Adjusting for proper order
with st.container():
    # Step 1: Image upload
    st.subheader("Step 1: Upload your image")
    uploaded_file = st.file_uploader("Choose an image to apply style", type=["jpg", "png"])

    if uploaded_file:
        # Step 2: Display uploaded image below upload box
        content_image = load_image(uploaded_file)
        st.subheader("Uploaded Image")
        st.image(content_image[0], caption="Uploaded Content Image", use_column_width=True)
        
        # Step 3: Style selection dropdown and submit button
        style_folder = 'art_styles'  # Set your art styles folder path
        style_images = load_style_images(style_folder)
        
        st.subheader("Step 2: Select a style")
        style_names = list(style_images.keys())
        selected_style = st.selectbox("Choose a style", style_names)

        if st.button("Generate Stylized Image"):
            if selected_style:
                # Load the selected style image
                selected_style_image = load_style_image(selected_style)
                
                # Apply style transfer
                stylized_image = apply_style_transfer(content_image, selected_style_image)
                
                # Convert the tensor to PIL Image and display it
                pil_image = tensor_to_pil(stylized_image)
                st.subheader(f"Result: {selected_style} Style")
                st.image(pil_image, caption=f"Stylized with {selected_style} Style", use_column_width=True)

# Art Style Transfer Web App

This is a **Streamlit-based** web application that allows users to apply artistic styles to their images using the **TensorFlow Hub** pre-trained style transfer model. Users can upload an image, select an art style from a dropdown menu, and see the transformed image in the chosen style.

## Features

- **Image Upload**: Users can upload their own image to be stylized.
- **Style Selection**: Users can choose from various art styles that are already preloaded in the system.
- **Stylized Image Generation**: Once the style is selected, the app applies the chosen style to the uploaded image and displays the output.
- **User-Friendly Interface**: Built with **Streamlit**, providing an interactive, responsive web interface.

## Technologies Used

- **Python**: Programming language used to implement the backend logic.
- **Streamlit**: Framework for building the interactive user interface.
- **TensorFlow**: Used for loading and applying the style transfer model.
- **TensorFlow Hub**: Provides access to a pre-trained style transfer model.
- **Pillow**: Used for image processing and display.

## Prerequisites

Make sure you have the following Python packages installed:
- `tensorflow`
- `tensorflow-hub`
- `streamlit`
- `numpy`
- `Pillow`
- `os`

How to Run the App
Clone the repository:

```bash
git clone https://github.com/yourusername/art-style-transfer-web-app.git
cd art-style-transfer-web-app
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```
Open your browser and go to http://localhost:8501 to view the app.

## How It Works
- Image Upload: The user uploads an image that will be transformed into an artwork.
- Style Selection: A dropdown menu lists available art styles. Users can select the desired style from the list.
- Style Transfer: The app applies the selected style to the uploaded image using a pre-trained style transfer model from TensorFlow Hub.
- Stylized Image: The stylized image is displayed on the page after the user clicks the "Generate Stylized Image" button.

## Art Styles
The art styles used in the app are stored in the art_styles folder. Each art style has a folder with a name representing the style, and within each folder, there is a style_image.jpg file that will be used for style transfer.

Feel free to add new art styles by adding more folders with style images in the art_styles directory

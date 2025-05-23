import streamlit as st
from PIL import Image
import numpy as np

# Set page title and layout
st.set_page_config(page_title="Spectrum Image Comparison", layout="wide")

# Add minimal CSS for styling
st.markdown("""
<style>
    h1, h3 {
        color: #1E3A8A;
    }
    .stSlider {
        padding-top: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.write("<h1>Spectrum Image Comparison</h1>", unsafe_allow_html=True)
st.write("<p>Use the slider to blend between images with and without spectral lines</p>", unsafe_allow_html=True)

# Cache the image loading to improve performance
@st.cache_data
def load_images():
    img_with_lines = Image.open('img/spectrum-of-a-g-type-star_en.png').convert('RGBA')
    img_without_lines = Image.open('img/spectrum-of-a-g-type-star_en-no-lines.png').convert('RGBA')
    return img_with_lines, img_without_lines

# Cache the image blending function to improve performance
@st.cache_data
def blend_images(img1, img2, alpha):
    return Image.blend(img1, img2, alpha)

try:
    # Load images (cached)
    img_with_lines, img_without_lines = load_images()
    
    # Create a single slider for both images
    alpha = st.slider("Blend Factor", 
                     min_value=0.0, 
                     max_value=1.0, 
                     value=0.5,
                     step=0.05,  # Larger step size for better performance
                     help="Move slider to blend between images with and without spectral lines")
    
    # Create two columns for side-by-side display
    col1, col2 = st.columns(2)
    
    # First column - Left image
    with col1:
        st.write("<h3>Original Image</h3>", unsafe_allow_html=True)
        st.image(img_with_lines, use_container_width=True, caption="With Spectral Lines")
    
    # Second column - Right image with blending
    with col2:
        st.write("<h3>Blended Image</h3>", unsafe_allow_html=True)
        # Blend images based on slider value (cached)
        blended_image = blend_images(img_without_lines, img_with_lines, alpha)
        st.image(blended_image, use_container_width=True, 
                caption=f"Blend Factor: {alpha:.2f}")
    
    # Add information about the images
    st.write("""
    <div style='margin-top: 20px;'>
        <h3>About These Images</h3>
        <p>These images show the spectrum of a G-type star. The left image shows the spectrum with spectral lines, 
        while the right image shows a blend between the versions with and without lines.</p>
        <p>The alpha channel blending allows for a smooth transition, making it easier to 
        identify the spectral lines and their positions.</p>
    </div>
    """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"Error loading or processing images: {e}")
    st.write("Please ensure the image files exist in the 'img' folder.")

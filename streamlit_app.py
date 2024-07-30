from PIL import Image
import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config("Ecolume Compost Image Comparer", "🪴")
st.header("🪴 Ecolume Compost Image Comparer")

# Upload two images
uploaded_images = st.file_uploader("Upload two images for comparison:", type=["jpg", "png"], accept_multiple_files=True)

if uploaded_images:
    if len(uploaded_images) == 2:
        img1, img2 = uploaded_images
        label1 = st.text_input("Label for the first image (e.g., Tank 1):", "Tank 1")
        label2 = st.text_input("Label for the second image (e.g., Tank 2):", "Tank 2")

        # Convert the uploaded images to PIL format
        img1_pillow = Image.open(img1)
        img2_pillow = Image.open(img2)

        # Display the comparison
        image_comparison(img1=img1_pillow, img2=img2_pillow, label1=label1, label2=label2)
    else:
        st.warning("Please upload exactly two images.")
else:
    st.info("Upload two images to compare.")

# Additional content (you can customize this part)
st.write("")
st.write("This is a reproduction of the fantastic WebbCompare app by John Christensen deployed in Streamlit ! Please support his repository if you like it !")

from PIL import Image
import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config("Webb Space Telescope vs Hubble Telescope", "🔭")
st.header("🔭 J. Webb Space Telescope vs Hubble Telescope")

# Upload two images
uploaded_images = st.file_uploader("Upload two images for comparison:", type=["jpg", "png"], accept_multiple_files=True)

if uploaded_images:
    if len(uploaded_images) == 2:
        img1, img2 = uploaded_images
        label1 = st.text_input("Label for the first image (e.g., Hubble):", "Hubble")
        label2 = st.text_input("Label for the second image (e.g., Webb):", "Webb")

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
st.write("This is a reproduction of the fantastic WebbCompare app by John Christensen. It's built in Streamlit and takes only 10 lines of Python code. If you like this app, please star John's original repo!")

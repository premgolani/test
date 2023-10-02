import os
import streamlit as st
import time
from PIL import Image, ImageDraw, ImageFont  # Import the necessary modules
from file_checker import checkFile
from PIL import Image, ImageDraw, ImageFont
import itertools  # Import the itertools module
import time

# Set the page title and icon
st.set_page_config(
    page_title="Malware Detection",
    page_icon=":shield:",
    layout="wide"  # Use wide layout for full-width content
)
# Add custom CSS to change the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #aaaddd; /* Set your desired background color here */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load the background image
background_image = Image.open('images/malware.png')

# Convert the image to RGB mode (full color)
background_image = background_image.convert('RGB')

# Create a drawing context
draw = ImageDraw.Draw(background_image)

# Define the font and size for the text
font_size = 70  # Adjust the font size as needed
font = ImageFont.load_default()  # You can customize the font here
font = ImageFont.truetype("arial.ttf", font_size)  # Use arial.ttf or another font file

font_size_new = 40  # Adjust the font size as needed
font_new = ImageFont.load_default()  # You can customize the font here
font_new = ImageFont.truetype("arial.ttf", font_size_new)  # Use arial.ttf or another font file

# Define the position and text to be added
text_position = (300, 100)  # Adjust the position as needed
text_position_new = (400, 200)  # Adjust the position as needed

text = "Live Malware Detection on any file"
textnew="Watch the epidemic as if it was on your computer"
# Define the initial text color (red)
text_color = (255, 0, 0)
# Add the text to the image
draw.text(text_position, text, fill="white", font=font)

draw.text(text_position_new, textnew, fill="red", font=font_new)
# Display the image with added text
st.image(background_image)

# Navigation sidebar
nav_option = st.sidebar.radio("Navigation", ["Home", "About Us"])

# Main title and description
if nav_option == "Home":
    st.title("Malware Detection")
    st.markdown(
        """
        Malwares can wreak havoc on a computer and its network. Hackers use it to steal passwords, delete files, and render computers inoperable. 
        A malware infection can cause many problems that affect daily operation and the long-term security of your company.
        """
    )

    # File upload section with animation
    file = st.file_uploader("Upload a file to check for malwares:", accept_multiple_files=True)
    if file:
        with st.spinner("Checking for malwares..."):
            # Simulate a delay for the spinner animation
            time.sleep(2)
            for uploaded_file in file:
                # Write the file to a temporary location
                with open('malwares/tempFile', 'wb') as f:
                    f.write(uploaded_file.getvalue())
                # Check if the file is legitimate or malware
                legitimate = checkFile("malwares/tempFile")
                os.remove("malwares/tempFile")
                # Display the result with animation
                if legitimate:
                    st.success(f"File {uploaded_file.name} seems *Good to use*!")
                else:
                    st.error(f"File {uploaded_file.name} is probably a **MALWARE**!!!")

elif nav_option == "About Us":
    st.title("About Us")
    st.markdown(
        """
        Welcome to our Malware Detection application! We are a team of cybersecurity experts dedicated to helping you protect your computer and network from malicious software.

        Our mission is to provide you with a reliable tool to check for malwares in your files. We understand the importance of cybersecurity and the potential threats that malwares pose to individuals and businesses.

        If you have any questions or feedback, please feel free to reach out to us. Your security is our top priority!
        """
    )

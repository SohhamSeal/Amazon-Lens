# Import necessary libraries
from PIL import Image
import requests
import io
import numpy as np
import easyocr

print("Applying OCR to image...")
image_url = "https://m.media-amazon.com/images/I/11gHj8dhhrL.jpg"


def extract_text_from_image_url(image):
    """
    Function to extract and clean text from an image URL using EasyOCR.

    Parameters:
    image_url (str): URL of the image.

    Returns:
    str: Cleaned extracted text with extra spaces and newlines removed.
    """
    try:
        reader = easyocr.Reader(['en'])
        text = reader.readtext(image, detail=0)
        
        # Joining  list of strings, remove extra spaces and newlines
        # clean_text = " ".join(text).strip()
        # clean_text = " ".join(clean_text.split())
        # clean_text = clean_text.replace('\n', ' ')
        return text
    except Exception as e:
        return f"An error occurred: {str(e)}"


image = Image.open(io.BytesIO(requests.get(image_url).content))
image = np.array(image)
print("Extracted text: ", extract_text_from_image_url(image))
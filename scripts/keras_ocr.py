# Import necessary libraries
import keras_ocr
import matplotlib.pyplot as plt
from PIL import Image
import requests
import io
import numpy as np

def read_image_from_url(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        image = keras_ocr.tools.read(io.BytesIO(response.content))
        predictions = keras_ocr.pipeline.recognize([image])
        return predictions[0]
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
        return None


print("Applying OCR to image...")

image_url = "https://m.media-amazon.com/images/I/110EibNyclL.jpg"

image = read_image_from_url(image_url)
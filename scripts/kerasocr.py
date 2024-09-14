# Import necessary libraries
import keras_ocr
import matplotlib.pyplot as plt
from PIL import Image
import requests
import io
import numpy as np

print("Applying OCR to image...")
image_url = "https://m.media-amazon.com/images/I/110EibNyclL.jpg"

image = keras_ocr.tools.read(io.BytesIO(requests.get(image_url).content))
predictions = keras_ocr.pipeline.recognize([image])
print(predictions[0])

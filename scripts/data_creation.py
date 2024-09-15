# Import necessary libraries
import numpy as np
import pandas as pd
from PIL import Image
import io
import requests
import pickle
import easyocr


# Variables
save_file_path = "/home/sealu/hackathon/Make-a-lens-for-Amazon/variables/"
file_path = "/home/sealu/hackathon/Make-a-lens-for-Amazon/variables/train.csv"
reader = easyocr.Reader(["en"])
n = 0
count = 0


# Functions
def extract_text_from_image(image):
    """
    Function to extract and clean text from an image URL using EasyOCR.
    Parameters:
    image (numpy array): nparray of the image.
    Returns:
    str: Extracted text with extra spaces and newlines removed.
    """
    try:
        text = reader.readtext(image, detail=0)
        text = " ".join(text)
        return text
    except Exception as e:
        return f"An error occurred: {str(e)}"


def load_image_from_url(image_url):
    """
    Downloads an image from a URL and converts it into a numpy array.
    Args:
      image_url (str): URL of the image to download.
    Returns:
      image_array (numpy array): The downloaded image as a numpy array.
    """
    try:
        print(f"Fetching image from {image_url}...")
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content))
            image = np.array(image)
            return image
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


# Main code

# Read the CSV file
df = pd.read_csv(file_path)
print("Dataframe loaded successfully...")
print("Total number of rows: ", df.shape[0])

# Pickling the dataframe
if n == 0:
    with open(save_file_path + "dataframe.pkl", "wb") as file:
        pickle.dump(df, file)
print(len(df))
print(df.head())

# df = df.iloc[n:]

# Iterate through the rows and create dictionaries
for index, row in df.iloc[n:].iterrows():
    if count == 200:
        break
    # print(index)
    print("Index:", index)
    image_matrix = load_image_from_url(row["image_link"])

    # Skipping non-accessible images
    if image_matrix is not None:
        df.loc[index,'image_link'] = extract_text_from_image(image_matrix) 
        # print("check:",df.iloc[n:index+1])
        print("Data extracted from image index: ", index)
    else:
        print("Skipping image index: ", index)
    count += 1

# with open(save_file_path + "testdf" + str(n) + ".pkl", "wb") as file:
#     pickle.dump(df.iloc[n:index], file)
    
df.to_csv(file_path, index=False)

print(df.iloc[:index].head())
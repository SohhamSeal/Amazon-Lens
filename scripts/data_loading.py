# Import necessary libraries
import numpy as np
import pandas as pd
from PIL import Image
import io
import requests
import pickle


# Variables
save_file_path = "/home/sealu/hackathon/Make-a-lens-for-Amazon/variables/"
file_path = "/home/sealu/hackathon/student_resource/dataset/train.csv"
n = 0


# Functions
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

def apply_ocr_to_image(image_matrix):
    print("Applying OCR to image...")
    

# Main code

# Read the CSV file
df = pd.read_csv(file_path)
print("Dataframe loaded successfully...")
print("Total number of rows: ", df.shape[0])

# # Pickling the dataframe
# with open(save_file_path + "dataframe.pkl", "wb") as file:
#     pickle.dump(df, file)

df = df.iloc[n:]

data_list = []

count = 0
# Iterate through the rows and create dictionaries
for index, row in df.iterrows():
    if count == 200:
        break
    image_matrix = load_image_from_url(row["image_link"])

    # Skipping non-accessible images
    if image_matrix is not None:
        # Create the dictionary
        data_dict = {
            "temp_id": index,
            "group_id": row["group_id"],
            "entity_name": row["entity_name"],
            "entity_value": row["entity_value"],
            "image_data": apply_ocr_to_image(image_matrix),
        }
        print("Data dictionary created for index: ", index)
        # Append the dictionary to the list
        data_list.append(data_dict)
        print("Appended data")
        with open(save_file_path + "data_list" + str(n) + ".pkl", "wb") as file:
            pickle.dump(data_list, file)
        print("Data dictionary saved for index: ", index)
        count += 1

"""
# Check if all the files have been saved
with open(save_file_path + "data_list.pkl", 'rb') as file:
    data_list_revived = pickle.load(file)

print("Data list loaded successfully...")
print("Total number of rows: ", len(data_list_revived))
"""

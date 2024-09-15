# Import necessary libraries
# import openai
from openai import OpenAI
import os
import sys
import pandas
import pickle
import csv

sys.path.append(os.path.abspath("/home/sealu/hackathon/Make-a-lens-for-Amazon/utils/"))
from constants import entity_unit_map
from dotenv import load_dotenv, find_dotenv

with open("/home/sealu/hackathon/Make-a-lens-for-Amazon/scripts/openaissh.py") as f:
    code = f.read()
exec(code)


# Variables
pickle_path = "/home/sealu/hackathon/Make-a-lens-for-Amazon/variables/df0.pkl"
test_pickle_path = "/home/sealu/hackathon/Make-a-lens-for-Amazon/variables/testdf0.pkl"
train_data_csv = "/home/sealu/hackathon/Make-a-lens-for-Amazon/variables/file.csv"
openai_sshkey = os.environ.get("OPENAI_SSHKEY")

# Functions

# Reading the CSV file and converting it to a formatted string
def read_csv_as_string(file_path):
    csv_string = ""
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_string += (
                ",".join(f'"{item}"' if "," in item else item for item in row) + "\n"
            )
    return csv_string.strip()  # To remove the trailing newline




# MAIN

# Load train dataset
with open(pickle_path, "rb") as file:
    train = pickle.load(file)
train_df = train[: int(len(train)/4)]
train_df.to_csv(train_data_csv)
train_string = read_csv_as_string(train_data_csv)

# Load test dataset
with open(test_pickle_path, "rb") as file:
    test = pickle.load(file)

memory_details = f"""
There is a pandas dataframe format that is mentioned in the following passage:
Read and understand the data. There are the following columns in the dataset:
image_link: this consists of the ocr data collected from an image (therefore, may contain some words with wrong spellings)
group_id: some id of a group the photo belonged to
entity_name: the name of the type of product
entity_value: the value that we require that is extracted from the image text obtained in 'image_link'

Use this dataset to understand the relation as to how the outputs(entity_value) is obtained.

You need to understand how the data is structured and how the outputs(entity_value) is obtained.
The entity_value is the value that we require that is extracted from the image text obtained in 'image_link'
entity_value has different types of outputs based on the following data: 
```{entity_unit_map}```

dataset to train on: 
```{train_string}```
"""

prompt = f"""
Your task is to act as a predictor model. use the memory details stated after this and predict the 'entity_value' for the following data:
{test.head(1)}.

You are given the following memory details:
Memory:
{memory_details}
"""


print(prompt)

# Using GPT-3
client = OpenAI()

completion = client.chat.completions.create(
    model="davinci-002",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": prompt,
        }
    ]
)

print(completion.choices[0].message)

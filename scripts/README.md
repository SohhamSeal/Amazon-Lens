This folder contains various Python scripts that are used to extract data from images and generate a suitable output format for the ML model.

The `data_loading.py` script is used to load the dataset into memory and create a pandas dataframe from it. It takes in the following parameters:

- `file_path`: The path to the dataset CSV file.
- `n`: The starting index of the dataframe.
- `count`: The number of rows to read from the dataframe.
- `save_file_path`: The path to save the created dataframe as a pickle file.

The `data_creation.py` script is used to create a new dataframe from the existing one. It takes in the following parameters:

- `file_path`: The path to the dataset CSV file.
- `n`: The starting index of the dataframe.
- `save_file_path`: The path to save the created dataframe as a pickle file.

The `kerasocr.py` script is used to extract text from images using the Keras OCR library. It takes in the following parameters:

- `image_url`: The URL of the image to extract text from.
- `output_filename`: The filename to save the extracted text as.

The `llm_usage.py` script is used to generate text using a large language model. It takes in the following parameters:

- `input_string`: The input string to generate text from.
- `prompt`: The prompt to generate text with.
- `model_name`: The name of the language model to use.

The `combine_variables.py` script is used to combine the variables from multiple pickle files into a single dataframe. It takes in the following parameters:

- `save_file_path`: The path to the folder containing the pickle files.

The `easyocr_usage.py` script is used to extract text from images using the EasyOCR library. It takes in the following parameters:

- `image_url`: The URL of the image to extract text from.
- `output_filename`: The filename to save the extracted text as.

The `test.ipynb` notebook is used to test the functions in the scripts folder. It takes in the following parameters:

- `DATASET_FOLDER`: The path to the dataset folder.

The `test.py` script is used to test the functions in the scripts folder. It takes in the following parameters:

- `DATASET_FOLDER`: The path to the dataset folder.

The `utils.py` script contains various utility functions used in the scripts folder. The functions are:

- `load_image_from_url(url)`: Loads an image from a given URL.
- `download_images(image_urls, folder_path)`: Downloads images from a list of URLs and saves them in a given folder.
- `parse_string(s)`: Parses a given string and returns a cleaned version of it.

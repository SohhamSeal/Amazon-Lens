# Amazon Lens
This repository contains code and data for the [repo](https://www.hackerearth.com/challenges/hackathon/make-a-lens-for-amazon-2/). The goal of the hackathon is to build a machine learning model that can extract information from product images and return structured data.

The dataset contains 2.6 million product images, each with a unique identifier. The images are stored in a publicly accessible bucket. The dataset also contains a CSV file that maps each image identifier to its corresponding product information.

The product information includes the product name, description, price, brand, and category, as well as the product's weight, dimensions, and other attributes. The attributes are represented as a JSON object, where each key is the attribute name and the value is the attribute value.

The task is to write a program that takes an image identifier as input, downloads the corresponding image from the bucket, extracts the relevant information from the image, and returns the extracted information in the same format as the product information CSV file.

The evaluation metric is the F1 score, which is the harmonic mean of precision and recall. The precision is the ratio of the number of true positives (i.e. the number of times the program correctly extracts a piece of information from an image) to the number of predicted positives (i.e. the number of times the program predicts that a piece of information is present in an image). The recall is the ratio of the number of true positives to the number of actual positives (i.e. the number of times the piece of information is actually present in the image).

The dataset is split into a training set and a test set. The training set contains 2.5 million images, and the test set contains 100,000 images. The test set is further divided into a public leaderboard set and a private leaderboard set. The public leaderboard set contains 10,000 images, and the private leaderboard set contains the remaining 90,000 images.

The program will be evaluated on the public leaderboard set, and the top 10 participants will be invited to submit their code to be evaluated on the private leaderboard set. The participant with the highest score on the private leaderboard set will be declared the winner.

The repository contains the following directories and files:

* `dataset/`: This directory contains the dataset. The dataset is divided into a training set and a test set. The training set is further divided into a public leaderboard set and a private leaderboard set. The public leaderboard set contains 10,000 images, and the private leaderboard set contains the remaining 90,000 images.
* `scripts/`: This directory contains the code for the hackathon. The code is written in Python, and uses the OpenCV library for image processing and the scikit-learn library for machine learning.
* `student_resource/`: This directory contains the code and data for the participants. The code is written in Python and is located in the `src/` directory. The data is located in the `dataset/` directory.

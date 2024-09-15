# Import necessary libraries
import pandas
import pickle

pickle_path = "/home/sealu/hackathon/Make-a-lens-for-Amazon/variables/df99.pkl"

with open(pickle_path, "rb") as file:
    df = pickle.load(file)
print(len(df))
print(df)

# with open(pickle_path, "wb") as file:
#     pickle.dump(df.iloc[:len(df)-1], file)
    
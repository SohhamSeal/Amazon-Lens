import pickle
import pandas as pd
import os

save_file_path = "/home/sealu/hackathon/Make-a-lens-for-Amazon/variables/"

list_of_files = [
    os.path.join(save_file_path, f)
    for f in os.listdir(save_file_path)
    if f.endswith(".pkl")
]

# Sort files based on creation time
sorted_files = sorted(list_of_files, key=os.path.getctime)
print(sorted_files)

df_files = []
for files in sorted_files:
    with open(files, "rb") as file:
        df_files.append(pickle.load(file))
    print("Done for ", files)

print(df_files[0])
# df_combined = pd.concat(df_files, axis=0, ignore_index=True)


# print(len(df_combined))


# with open(save_file_path + "df_combined.pkl", "wb") as file:
#     pickle.dump(df_combined, file)

# df_combined

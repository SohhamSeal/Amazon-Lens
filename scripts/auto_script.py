# Import necessary libraries
import pandas as pd

# Variables
N = 1198
prevN = 0

with open("/home/sealu/hackathon/Make-a-lens-for-Amazon/scripts/data_loading.py") as f:
    code = f.read()

while N < 263859:
    code = code.replace(f"n = {prevN}", f"n = {N}")
    # print(code)
    exec(code)
    prevN = N
    N += 249
    print(f"\nDone from [{prevN}-{N}]")

# Import necessary libraries
import pandas as pd

# Variables
N = 0
prevN = 0

with open("/home/sealu/hackathon/Make-a-lens-for-Amazon/scripts/data_creation_test.py") as f:
    code = f.read()

while N < 131187:
    code = code.replace(f"n = {prevN}", f"n = {N}")
    # print(code)
    exec(code)
    prevN = N
    N += 100
    print(f"\nDone from [{prevN}-{N}]")

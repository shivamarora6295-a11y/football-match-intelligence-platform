import pandas as pd

path = r"C:\Football_AI_Project\datasets\datasets\martj42\international-football-results-from-1872-to-2017\versions\138"

df = pd.read_csv(path + r"\results.csv")

print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)
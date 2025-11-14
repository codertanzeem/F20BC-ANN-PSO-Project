#Load the Dataset
import pandas as pd
df = pd.read_csv("concrete_data.csv")

print(df.head())

# Basic stats
print(df.describe())
print(df.isnull().sum())


import matplotlib.pyplot as plt


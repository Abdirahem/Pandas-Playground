import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('people100.csv')
print(df.head())
print(df.tail())

search_name = 'Shelby'
matching_rows = df[df['First Name'].str.contains(search_name, case=False, na=False)]
print(f"Rows matching '{search_name}':")
print(matching_rows)
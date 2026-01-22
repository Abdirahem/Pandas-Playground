import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('people100.csv')


search_name = 'Shelby'
matching_rows = df[df['First Name'].str.contains(search_name, case=False, na=False)]
print(f"Rows matching '{search_name}':")
print(matching_rows)

search_name = 'Dennis'
matching_rows = df[df["First Name"].str.contains(search_name,case=False,na=False)]
print(f"Rows matching '{search_name}':")
print(matching_rows)
df.loc[matching_rows.index, "First Name"] = "Hem"
print(df.tail())
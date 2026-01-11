import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'people100.csv'
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)
# Display the first few rows of the DataFrame
data_frame = pd.read_csv(file_path)
# Show the first 5 rows of the DataFrame
result = data_frame.head()
# Display the result
print(result)
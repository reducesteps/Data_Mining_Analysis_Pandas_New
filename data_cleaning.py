import pandas as pd

# Load the dataset
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Remove missing values
data.dropna(inplace=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

# Save the cleaned data
data.to_csv('cleaned_data.csv', index=False)

print('Data cleaning completed.')
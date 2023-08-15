import pandas as pd

# Load the cleaned data
file_path = 'cleaned_data.csv'
data = pd.read_csv(file_path)

# Perform some basic analysis
mean_value = data['value_column'].mean()
max_value = data['value_column'].max()
min_value = data['value_column'].min()

print('Mean Value:', mean_value)
print('Max Value:', max_value)
print('Min Value:', min_value)
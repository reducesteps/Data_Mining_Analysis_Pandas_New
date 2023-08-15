import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
file_path = 'cleaned_data.csv'
data = pd.read_csv(file_path)

# Create a simple plot
plt.plot(data['value_column'])
plt.title('Value Plot')
plt.xlabel('Index')
plt.ylabel('Value')

# Show the plot
plt.show()
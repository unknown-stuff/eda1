import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sample datasets
data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Alice', 'Bob', 'Charlie', 'Eva'],
    'Age': [25, 30, np.nan, 40, 35]
}

data2 = {
    'ID': [6, 7, 8, 9, 10],
    'Name': ['Frank', 'David', 'Alice', 'Bob', 'Emily'],
    'Age': [45, 50, 28, np.nan, 40]
}

# Convert dictionaries to DataFrames
dataset1 = pd.DataFrame(data1)
dataset2 = pd.DataFrame(data2)

# Save datasets to CSV files
dataset1.to_csv('dataset1.csv', index=False)
dataset2.to_csv('dataset2.csv', index=False)

# Load datasets
dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')

# Data Cleaning
# Remove missing values
dataset1_cleaned = dataset1.dropna()
dataset2_cleaned = dataset2.dropna()

# Remove duplicates
dataset1_cleaned = dataset1_cleaned.drop_duplicates()
dataset2_cleaned = dataset2_cleaned.drop_duplicates()

# Data Integration
# Concatenate datasets
merged_dataset = pd.concat([dataset1_cleaned, dataset2_cleaned], ignore_index=True)

# Save the merged dataset to a new CSV file
merged_dataset.to_csv('merged_dataset.csv', index=False)

print("Data cleaning and integration completed.")

# Visualization - Histogram
plt.figure(figsize=(10, 6))
plt.hist(dataset1_cleaned['Age'], bins=10, alpha=0.5, label='Dataset 1')
plt.hist(dataset2_cleaned['Age'], bins=10, alpha=0.5, label='Dataset 2')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Ages')
plt.legend()
plt.grid(True)
plt.show()

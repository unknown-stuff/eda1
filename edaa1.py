import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset from seaborn
iris_df = sns.load_dataset('iris')

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris_df, hue='species', palette='Set1')
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.grid(True)
plt.legend(title='Species')
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
iris_species_counts = iris_df['species'].value_counts()
plt.pie(iris_species_counts, labels=iris_species_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Iris Species Distribution')
plt.axis('equal')
plt.show()

# Line chart
plt.figure(figsize=(10, 6))
sns.lineplot(data=iris_df.drop(columns='species'))
plt.title('Line Chart of Iris Measurements')
plt.xlabel('Samples')
plt.ylabel('Measurements')
plt.legend(title='Attributes', loc='upper right', labels=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
plt.grid(True)
plt.show()

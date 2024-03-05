import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset from seaborn
iris_df = sns.load_dataset('iris')

# Heatmap
plt.figure(figsize=(10, 6))
corr = iris_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix for Iris Dataset')
plt.show()

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris_df, palette='Set3')
plt.title('Box Plot of Iris Dataset')
plt.ylabel('Measurements')
plt.xlabel('Features')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
iris_df.hist(edgecolor='black', linewidth=1.2, figsize=(12, 8))
plt.suptitle('Histograms of Iris Dataset Features')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (replace this with your own dataset)
import pandas as pd
data = pd.read_csv(r'C:\Users\enrique.silva\Documents\Python Scripts\iris.csv')


print(data.head())

sns.histplot(data=data, x='sepal.length', bins=20, kde=True)
plt.title('Distribution of Sepal')
plt.show()


sns.pairplot(data=data, hue='sepal.length', diag_kind='hist')
plt.suptitle('Pairwise Relationships')
plt.show()

sns.boxplot(data=data, x='category_column', y='numeric_column')
plt.title('Box Plot')
plt.show()


correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


sns.countplot(data=data, x='category_column', hue='hue_column')
plt.title('Count Plot')
plt.show()

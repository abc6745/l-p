import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("ML_dataset_sales_data_sample.csv", encoding='latin1')

print("Dataset preview:")
print(data.head())

print("\nInformation of Dataset: ")
print(df.info())

print("\nShape of Dataset: ")
print(df.shape)

print("\nColumn names in Dataset: ")
print(df.columns)

print("\nTotal elements in Dataset: ")
print(df.size)

print("\nDatatype of attributes(columns): ")
print(df.dtypes)

print("\nFirst 5 rows: ")
print(df.head(5).T)

print("\nLast 5 rows: ")
print(df.tail(5).T)

print("\nAny 5 rows: ")
print(df.sample(5).T)

print("\nStastical Information of Dataset: ")
print(df.describe())

print("\nTotal null elements in Dataset: ")
print(df.isna().sum())

numeric_features = ['QUANTITYORDERED', 'PRICEEACH', 'SALES', 'MSRP']
X = data[numeric_features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8,5))
plt.plot(K, inertia, 'bo-')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.show()

optimal_k = 3 

kmeans = KMeans(n_clusters=optimal_k, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

print("\nClustered Data Sample:")
print(data[['QUANTITYORDERED', 'PRICEEACH', 'SALES', 'MSRP', 'Cluster']].head())

plt.figure(figsize=(8,6))
plt.scatter(X_scaled[:,0], X_scaled[:,2], c=data['Cluster'], cmap='viridis')
plt.title('K-Means Clusters (Sales vs Quantity Ordered)')
plt.xlabel('Quantity Ordered (scaled)')
plt.ylabel('Sales (scaled)')
plt.show()

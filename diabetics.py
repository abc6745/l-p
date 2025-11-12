import pandas as pd 
import numpy as np  
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

df=pd.read_csv('diabetics.csv')
 
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

X=df.drop('Outcome', axis=1)
y=df['Outcome']
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=42)

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)

conf_matrix=confusion_matrix(y_test,y_pred)
accuracy=accuracy_score(y_test,y_pred)
error=1-accuracy
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)

print("K-Neighbors Classifier")
print(f"Confusion Matrix: {conf_matrix}")
print(f"Accuracy: {accuracy:.4f}")
print(f"Error: {error:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
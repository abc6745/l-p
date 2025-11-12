import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df=pd.read_csv('uber.csv')

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

df.drop(['Unnamed: 0', 'key'], axis=1, inplace=True)

df.dropna(inplace=True)

df['pickup_datetime']=pd.to_datetime(df['pickup_datetime'])

df=df.dropna(subset=['pickup_datetime'])

df['hour']=df['pickup_datetime'].dt.hour
df['day']=df['pickup_datetime'].dt.day
df['month']=df['pickup_datetime'].dt.month
df['year']=df['pickup_datetime'].dt.year
df['weekday']=df['pickup_datetime'].dt.weekday

df.drop('pickup_datetime',axis=1, inplace=True)

df=df[(df['fare_amount']>0) & (df['passenger_count']>0) & (df['passenger_count']<8)]

plt.figure(figsize=(6,4))
sns.boxplot(x=df['fare_amount'], color='skyblue')
plt.title("Fare Amount before outlier removal")
plt.show()

q_low=df['fare_amount'].quantile(0.01)
q_high=df['fare_amount'].quantile(0.99)
df=df[(df['fare_amount']>=q_low) & (df['fare_amount']<=q_high)]

plt.figure(figsize=(6,4))
sns.boxplot(x=df['fare_amount'], color='skyblue')
plt.title("Fare Amount after outlier removal")
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correration Heatmap")
plt.show()

X=df.drop('fare_amount', axis=1)
y=df['fare_amount']

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)

lr=LinearRegression()
lr.fit(X_train,y_train)
lr_pred=lr.predict(X_test)

lr_rmse=np.sqrt(mean_squared_error(y_test, lr_pred))
lr_mae=mean_absolute_error(y_test,lr_pred)
lr_r2=r2_score(y_test,lr_pred)
lr_mape=np.mean(abs((y_test-lr_pred)/y_test))*100

print("Liner Regression Results")
print(f"RMSE: {lr_rmse:.4f}")
print(f"MAE: {lr_mae:.4f}")
print(f"R2 Score: {lr_r2:.4f}")
print(f"MAPE %: {lr_mape:.2f}")

rf=RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train,y_train)
rf_pred=rf.predict(X_test)

rf_rmse=np.sqrt(mean_squared_error(y_test,rf_pred))
rf_mae=mean_absolute_error(y_test,rf_pred)
rf_r2=r2_score(y_test,rf_pred)
rf_mape=np.mean(abs((y_test-rf_pred)/y_test))*100

print("Ramdom Forest Regressor Results")
print(f"RMSE: {rf_rmse:.4f}")
print(f"MAE: {rf_mae:.4f}")
print(f"R2 Score: {rf_r2:.4f}")
print(f"MAPE %: {rf_mape:.2f}")

results=pd.DataFrame({
	"Model":["LinearRegression", "RandomForestRegressor"],
	"RMSE":[lr_rmse,rf_rmse],
	"MAE":[lr_mae,rf_mae],
	"R2 Score":[lr_r2,rf_r2],
	"MAPE":[lr_mape,rf_mape]
	})
print("Model Comparison")
print(results)
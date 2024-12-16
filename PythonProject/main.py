import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

pd.set_option('display.max_columns', 12)
pd.options.display.width= None
pd.options.display.max_columns= None

#Loading the data frame
data_frame = pd.read_csv('data/Walmart_Sales.csv')
df = pd.DataFrame(data_frame)
print(df.head(5),'\n')

#checking for missing values
missing_values = df.isna()
print('There is ', missing_values.sum(),'missing values\n')
#checking for duplicated values
duplicates = df.duplicated()
print('There is ', duplicates.sum(),'duplicated values\n')

#data description
described_data = df.describe()
print(described_data,'\n')

#converting date to usable data
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

df['Day'] = df['Date'].dt.day
df.insert(2, 'Day', df.pop('Day'))
df['Month'] = df['Date'].dt.month
df.insert(3, 'Month', df.pop('Month'))
df['Year'] = df['Date'].dt.year
df.insert(4, 'Year', df.pop('Year'))
df['Day of Week'] = df['Date'].dt.day_name()
df.insert(5, 'Day of Week', df.pop('Day of Week'))
print(df.head(5),'\n')
described_data = df.describe()
print(described_data,'\n')

#EDA
x=0
y= df['Weekly_Sales'].sum()
print('total number of sales: ',df['Weekly_Sales'].sum(),'\n')
for store, store_data in df.groupby('Store'):
        average = store_data['Weekly_Sales'].mean()
        if average > x:
                x = average
                i = store
        if average < y:
                y = average
                s = store

        print(f'Store {store}: Average Weekly sales: {average.round(2)}')
print(f'\nThe store with the biggest average weekly sales was: {i}, with {x.round(2)} sales\n')
print(f'The store with the lowest average weekly sales was: {s}, with {y.round(2)} sales\n')

#
#CorrelationMatrix
numeric_df = df.select_dtypes(include=['number'])
crr_matrix = numeric_df.corr()
crr_matrix = crr_matrix.drop(columns=['Weekly_Sales'], errors='ignore', axis=1)
crr_matrix = crr_matrix.drop(index=['Day','Date','Store','Month', 'Year', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment' ], errors='ignore', axis=0)
plt.figure(figsize=(15, 2))
sns.heatmap(crr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
#Comparing sales to weeks with holiday and weeks without holidays
        #total sales
holiday = df[df['Holiday_Flag'] == 1]['Weekly_Sales'].sum()
notholiday = df[df['Holiday_Flag'] == 0]['Weekly_Sales'].sum()
plt.bar(['Holiday', 'Non-Holiday'], [holiday, notholiday])
plt.title("Total Sales: Holiday vs Non-Holiday")
plt.ylabel("Total Weekly Sales")
plt.show()
        #average sales
holiday = df[df['Holiday_Flag'] == 1]['Weekly_Sales'].mean()
notholiday = df[df['Holiday_Flag'] == 0]['Weekly_Sales'].mean()
plt.bar(['Holiday', 'Non-Holiday'], [holiday, notholiday])
plt.bar(['Holiday', 'Non-Holiday'], [holiday, notholiday])
plt.title("Average Sales: Holiday vs Non-Holiday")
plt.ylabel("Average Weekly Sales")
plt.show()

#









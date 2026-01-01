from sqlite3.dbapi2 import Time
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
# sales = pd.Series([250, 150, 300, 400])
# print(sales)
# print(sales[0:2])
# print(sales.index)
# print(sales.values)
# print(sales.dtype)
# print(sales.head(1))
# print(sales.tail(1))
# print(sales.sort_values())
# print(sales.count())
# sales1 = pd.Series([1, 2, None, 4])
# print(sales1.isnull())
# print(sales1.notnull())

# print(sales1 + 2 )
# print(sales1 * 2 )
# print(sales1 / 2 )  
# print(sales1 - 2 )
# print(sales1 ** 2 )
# print(sales1 // 2 )
# print(sales1.fillna(0))


# Create DATA Frame
# data = {
#     'Name': ['Umer', 'ALi', 'Ahmed', 'Usman'],
#     'Age': [22, 24, 35, 32],
#     'City': ['New York', 'Paris', 'Berlin', 'London']
    
# }

# df = pd.DataFrame(data)
# print(df)

# DATASET1 =pd.Series (data=[1, 2, 3, 4, 5])  
# DATASET2 =pd.Series (data=[6, 7, 8, 9, 10])  
# CheckCol = pd.DataFrame({'Col1': DATASET1, 'Col2': DATASET2})
# print(CheckCol)
# print(CheckCol.shape)
# print(CheckCol.columns)
# print(CheckCol.dtypes)
# print(CheckCol.loc[2, 'Col1'])
# print(CheckCol.loc[2, 'Col2'])
# print(CheckCol.iloc[2, 0])
# print(CheckCol.iloc[2, 1])  
# print(CheckCol.head(2))
# print(CheckCol.tail(2))
# print(CheckCol.count())
# print(CheckCol.info())
# print(CheckCol.describe())

# DATA FILTERING
# print(CheckCol[CheckCol['Col1'] == 2])
# print(CheckCol[CheckCol['Col2'] > 8])
# print(CheckCol[(CheckCol['Col1'] > 2) & (CheckCol['Col2'] < 9)])
# print(CheckCol[(CheckCol['Col1'] < 2) | (CheckCol['        Col2'] > 9)])


# Adding , Updating & Deleting Columns
# CheckCol['Col3'] = ([11, 12, 13, 14, 15])
# print(CheckCol)

# CheckCol = CheckCol.drop(columns=['Col3'])
# print(CheckCol)

# CheckCol.loc[CheckCol["Col1"] == 2, ] = 20
# print(CheckCol)
# CheckCol.rename(columns={'Col1': 'Column1', 'Col2': 'Column2'}, inplace=True)
# print(CheckCol)


# Indexing And Selecting Data
# CheckCol.set_index('Col1', inplace=True)
# print(CheckCol)

# CheckCol['Col3'] = (['a', 'b', 'c', 'd', 'e'])
# print(CheckCol)

# CheckCol['Col4'] = (['f', 'g', 'h', 'i', 'j'])
# print(CheckCol)


# CheckCol.reset_index(inplace=True)
# print(CheckCol)

# Multi Index

# Multi_Data = pd.DataFrame({
#     'City': ['New York', 'New York', 'Paris', 'Paris', 'Berlin', 'Berlin'],
#     'Year': [2020, 2021, 2020, 2021 , 2020, 2021],
#     'Sales': [250, 300, 150, 200, 300, 350]
# })
# Multi_Data.set_index(['City', 'Year'], inplace=True)
# print(Multi_Data)

# Multi_Data[Multi_Data['Sales'] > 300]
# print(Multi_Data)

# Multi_Data.query('Year > 2020 and Sales > 300', inplace=True)
# print(Multi_Data)

# Working With Data Files
# df = pd.read_csv('data.csv')

# Multi_Data.to_csv('multi_data.csv', index=False)
# df = pd.read_csv('multi_data.csv')

# report = pd.read_csv('report.csv')
# report.to_csv('Umer.csv', index=False)
# data = pd.read_csv('Umer.csv')
# print(data)

# Data as a dictionary
# data_dict = {'x':[1, 2, 3, 4, 5], 'y': np.array([10, 20, 30, 40, 50]),'z':60}
# df = pd.DataFrame(data_dict)
# print(df)

# TwoD_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# df2 = pd.DataFrame(TwoD_array, columns=['Column1', 'Column2', 'Column3'])
# print(df2)


# Numpy_array = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15]])
# df3 = pd.DataFrame(Numpy_array, columns=['A', 'B', 'C', 'D', 'E'])
# print(df3)



# Data Cleaning and Processing
# data = {
#     'Name': ['Umer', 'Ali', None, 'Usman', 'Ahmed', None],
#     'Age': [22, 24, 35, None, 32, 28],
#     'City': ['New York', None, 'Berlin', 'London', 'Paris', 'Tokyo']
# }
# df = pd.DataFrame(data)
# print(df)
# df.dropna(inplace=True)
# df.fillna(0, inplace=True)
# print(df)

# DATASET1 = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5, 6],
#     'B': [10, 20, 30, 40, 50, 60],
#     'C': [100, 200, 300, 400, 500, 600]
# })  

# print(DATASET1.mean())
# print(DATASET1.median())
# print(DATASET1.mode())
# print(DATASET1.std())
# print(DATASET1.min())
# print(DATASET1.max())


# Remove Duplicates
# data = {    
#     'Name': ['Umer', 'Umer', 'Ahmed', 'Umer', 'Usman', 'Ali'],
#     'Age': [22, 22, 35, 22, 32, 24],
#     'City': ['New York', 'New York', 'Berlin', 'New York', 'London', 'Paris']
# }
# df = pd.DataFrame(data)
# print(df.drop_duplicates())
# print(df.replace('Umer', 'Hassan'))

# Type Conversion
# data = {
#     'Name': ['Umer', 'Ali', 'Ahmed', 'Usman'],
#     'Age': ['22', '24', '35', '28'],
#     'City': ['New York', 'Paris', 'Berlin', 'London']
# }
# df = pd.DataFrame(data)
# df['Age'] = df['Age'].astype(float)
# print(df.dtypes)
# print(df['Age'].dtype)

# string operations
# df['Name'] = df['Name'].str.upper()
# print(df['Name'])


# Data Aggregation and Grouping
# data = {
#     'City': ['New York', 'New York', 'Paris', 'Paris', 'Berlin', 'Berlin'],
#     'Year': [2020, 2021, 2020, 2021, 2020, 2021],
#     'Sales': [250, 300, 150, 200, 300, 350]
# }
# df = pd.DataFrame(data)
# grouped = df.groupby('City')
# print(grouped['Sales'].sum())   
# print(grouped['Sales'].mean())
# print(grouped['Sales'].max())
# print(grouped['Sales'].min())
# print(grouped['Sales'].count())
# print(grouped['Sales'].std())




# DATA MANIPULATION WITH PANDAS
# Merging DataFrames
# data1 = {
#     'ID': [1, 2, 3, 4],
#     'Name': ['Umer', 'Ali', 'Ahmed', 'Usman']

# }
# data2 = {
#     'ID': [3, 4, 5, 6],
#     'Age': [35, 32, 28, 24]
# }
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# merged = pd.merge(df1, df2, on='ID', how='inner')
# print(merged)

# csv files large data handling
# df = pd.read_csv('report.csv', chunksize=1000)
# for chunk in df:
#     print(chunk.head())
#     print(chunk.describe())
#     print(chunk.info())

# data = {
#     'Name': ['Umer', 'Ali', 'Ahmed', 'Usman'],
#     'Age': [22, 24, 35, 32],
#     'City': ['New York', 'Paris', 'Berlin', 'London']  
# }

# df = pd.DataFrame(data)
# print(df)
# pivot = pd.pivot_table(df, values='Age', index='Name')
# print(pivot)
# crosstab = pd.crosstab(df['Name'], df['City'])
# print(crosstab) 

# Merging joining and concatenating
# data1 = {
#     'Name': ['Umer', 'Ali', 'Ahmed', 'Usman'],
#     'ID': [1, 2, 3, 4]
# }
# data2 = {
#     'Name': ['Umer', 'Ali', 'Ahmed', 'Usman'],
#     'ID': [3, 4, 5, 6]
  
# }
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# checkConcat = pd.concat([df1, df2], axis=1)
# print(checkConcat)
# checkJoin = df1.join(df2)
# print(checkJoin)
# merged = pd.merge(df1, df2, on='Name')
# print(merged)
# join = df1.set_index('Name').join(df2.set_index('Name'), lsuffix='_left', rsuffix='_right')
# print(join)

# Working with Time Series


# Simple time series data
data = {
    "Date": pd.date_range(start="2025-01-01", periods=6, freq="D"),
    "Name": ["Umer", "Ali", "Umer", "Ali", "Umer", "Ali"],
    "Sales": [100, 150, 120, 180, 130, 200]
}

df = pd.DataFrame(data)
print("Original Data:")
df.set_index('Date', inplace=True)
# print(df)

# dateee = pd.to_datetime('2025-04-29')
# print(dateee)
# # Resampling
# resampled = df.resample('2D').sum()
# print(resampled)
# weekly = df.resample('W').sum()
# print(weekly)   

# shifting lagging
# shifted = df.shift(2)
# print("Shifted Data:")

# print(shifted)


# Rolling Calculations
# rolling =  df['Rolling Average'] = df['Sales'].rolling(window=2).mean()
# print(rolling)



#  Data Visualization
plot =  df['Sales'].plot()
print(plot)
data['df'].plot(kind='line')
data['df'].plot(kind='bar')
data['df'].plot(kind='barh')
data['df'].plot(kind='hist')
data['df'].plot(kind='box')
data['df'].plot(kind='scatter', x='Date', y='Sales') #provide x&y axis data
data['df'].plot(kind='area')
data['df'].plot(kind='pie')

plt.show()  


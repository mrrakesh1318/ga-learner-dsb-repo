# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




#Code starts here

# Loading the data
data =pd.read_csv(path)

# Plotting a histogram for Rating feature
#plt.hist(data['Rating'])
#plt.xlabel("App Rating")
#plt.show()
data['Rating'].plot(kind='hist')

# Masking rating >5
mask =data['Rating'] <= 5

# Applying mask
data =data[mask]
print("="*50)
# Visualizing after applying mask
# fig =figure(figsize =(8,10))
plt.hist(data['Rating'])
plt.show()

#Code ends here


# --------------
# code starts here

# Series containingcount of total count of null values
total_null =data.isnull().sum()

# Percenatge of null values in the data
percent_null =(total_null/data.isnull().count()) *100
# print(percent_null)

missing_data =pd.concat((total_null,percent_null), keys=['Total','Percent'], axis=1)
print(missing_data)

# Dropping null values
data.dropna(inplace =True)

# Checking for null values
total_null_1 =data.isnull().sum()
percent_null_1 =(total_null_1/data.isnull().count()) *100
missing_data_1 =pd.concat((total_null_1, percent_null_1), keys=['Total', 'Percent'], axis =1)
print(missing_data_1)

# code ends here


# --------------

#Code starts here

# Plotting Rating to check for category
sns.catplot(x='Category', y='Rating', data =data, kind ="box", height =10)
plt.xticks(rotation =90)
plt.title("Rating vs Category[BoxPlot]")


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

# Inspect Installs column
print(data['Installs'].value_counts())

# Converting Install column to int
data['Installs']=data['Installs'].apply(lambda x:x.replace(',',"")).apply(lambda x:x.replace('+','')).astype(int)

# Encoding using LabelEncoder
le =LabelEncoder()

# Tranforming Installs column 
data['Installs'] =le.fit_transform(data['Installs'])

# Plotting using seaborn
sns.regplot(x ='Installs', y='Rating', data =data)
plt.title("Rating vs Installs[RegPlot]")
plt.show()

#Code ends here



# --------------
#Code starts here

# Checking the values of Price column
print(data['Price'].value_counts())

# Removing $ from Price column
data['Price'] =data['Price'].str.replace("$","")

# Changing type to float
data['Price'] =data['Price'].astype(float)

plt.figure(figsize =(10,10))
sns.regplot(x ='Price', y='Rating', color ='green', data=data)
plt.title('Rating vs Price' ,size=15)
plt.show()
#Code ends here


# --------------

#Code starts here

# Unique values of Genre column
print(data['Genres'].unique())

# Apllying str.split() on genre column
data['Genres'] =data['Genres'].str.split(';')

# Function to get only the first element from list
def getlist_item(a):
    a =a[0]
    return a

# Applying the function on Genres column
data['Genres'] =data['Genres'].apply(getlist_item)

# Grouping genres and  ratings by genres and getting mean 
gr_mean =data[['Genres','Rating']].groupby('Genres', as_index =False).mean().round(2)

# Checking the statistics of gr_mean
print(gr_mean.describe())

# Sorting the gr_mean by Rating
gr_mean =gr_mean.sort_values(by ='Rating')

# Top and bottom genres by rating
print(gr_mean.iloc[0])
print(gr_mean.iloc[-1])

#Code ends here


# --------------

#Code starts here

# Last Updated column
print(data['Last Updated'].head())

# Converting to data time format
data['Last Updated'] =pd.to_datetime(data['Last Updated'])

# Getting maximum date(most recent date)
max_date =max(data['Last Updated'])

# Adding a Last Updated Days column to the dataframe
data['Last Updated Days'] =(max_date -data['Last Updated']).dt.days

# Plotting Rating vs Last Updated
plt.figure(figsize =(15,10))
sns.regplot(x='Last Updated Days', y='Rating', color ='orange', data =data)
plt.title("Rating vs Last Updated [Regplot]", size =20)
plt.show()
#Code ends here



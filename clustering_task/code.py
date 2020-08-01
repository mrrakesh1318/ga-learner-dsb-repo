# --------------
# import packages

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 



# Load Offers
offers =pd.read_excel(path, sheet_name =0)

# Load Transactions
transactions =pd.read_excel(path, sheet_name =1)

# adding 'n' to transactions
transactions['n'] =1

# Merge dataframes
# merging two dataframes on a common attribute
# in our case 'Offer#' is the common attribute
df =transactions.merge(offers)

# Look at the first 5 rows
print(df.head())


# --------------
# Code starts here

# create pivot table
matrix =pd.pivot_table(df, index ='Customer Last Name', columns ='Offer #',
values ='n')

# replace missing values with 0
matrix.fillna(0, inplace =True)

# reindex pivot table
matrix.reset_index(inplace =True)

# display first 5 rows
print(matrix.head())

# Code ends here


# --------------
# import packages
from sklearn.cluster import KMeans

# Code starts here

# initialize KMeans object
cluster =KMeans(n_clusters =5, init ='k-means++', max_iter =300,
n_init =10, random_state =0)

# create 'cluster' column
matrix['cluster'] =cluster.fit_predict(matrix[matrix.columns[1:]])

# assigning cluster centers
print(matrix.head())
# Code ends here


# --------------
# import packages
from sklearn.decomposition import PCA

# Code starts here

# initialize pca object with 2 components
pca =PCA(n_components =2, random_state =0)

# create 'x' and 'y' columns donoting observation locations in decomposed form
matrix['x'] =pca.fit_transform(matrix[matrix.columns[1:]])[:,0]
matrix['y'] =pca.fit_transform(matrix[matrix.columns[1:]])[:,1]

# dataframe to visualize clusters by customer names
clusters =matrix.iloc[:,[0,33,34,35]]

# visualize clusters
plt.scatter(x='x', y='y', data=clusters, cmap ='virdis')
plt.show()

# Code ends here


# --------------
# Code starts here

# merge 'clusters' and 'transactions'
data =transactions.merge(clusters)

# merge `data` and `offers`
data =data.merge(offers)

# initialzie empty dictionary
champagne ={}

# iterate over every cluster
for i in range(0,5):

    # observation falls in that cluster
    new_df =pd.DataFrame(data[data['cluster'] ==i])

    # sort cluster according to type of 'Varietal'
    counts =new_df['Varietal'].value_counts(ascending =False)

    # check if 'Champagne' is ordered mostly
    if counts.index[0] =="Champagne":

        # add it to 'champagne'
        champagne.update({i :counts[0]})

# get cluster with maximum orders of 'Champagne' 
cluster_champagne =max(champagne, key =champagne.get)

# print out cluster number
print("The Cluster with most number of Champagne purchase ",cluster_champagne)



# --------------
# Code starts here

# empty dictionary
discount ={}
print(data.head())
print('=' *50)

# iterate over cluster numbers
for val in data['cluster'].unique():

    # dataframe for every cluster
    new_df =data[data['cluster'] ==val]

    # average discount for cluster
    counts =(new_df['Discount (%)'].sum())/len(new_df)

    # adding cluster number as key and average discount as value 
    discount[val] =counts

# cluster with maximum average discount
cluster_discount =max(discount, key =discount.get)

print("The Cluster with maximum average discounts")
# Code ends here



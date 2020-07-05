# --------------
import pandas as pd
from sklearn import preprocessing

#path : File path

# Code starts here


# read the dataset
dataset =pd.read_csv(path)

# look at the first five columns
print(dataset.head())

# Check if there's any column which is not useful and remove it like the column id
dataset.drop('Id', inplace= True, axis =1)

# check the statistical description
print(dataset.describe())


# --------------
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt

#names of all the attributes 
cols = dataset.columns

#number of attributes (exclude target)
size = len(cols) - 1

#x-axis has target attribute to distinguish between classes
x =dataset['Cover_Type'].copy()

#y-axis shows values of an attribute
y =dataset.drop('Cover_Type', axis =1)

#Plot violin for all attributes
for i in range(0,size):
        col = cols[i]
        #sns.violinplot(x=x, y=cols[i], data =dataset, ax=axes[i])
        sns.violinplot(data=dataset,x=x,y=y[col])
#plt.show()



# --------------
import numpy
upper_threshold = 0.5
lower_threshold = -0.5


# Code Starts Here

# Getting the first 10 features
subset_train = dataset.iloc[:,0:10]

# Correlation among the 10 features
data_corr =subset_train.corr()

# Plotting a heatmap of correlation matrix
sns.heatmap(data_corr)

# unstacking the data_corr
correlation =data_corr.unstack().sort_values(kind ='quicksort')

# Slicing the correlation variable upon the threshold values
corr_var_list =[]
for i in correlation:
    if i < lower_threshold:
        corr_var_list.append(i)
    elif i > upper_threshold and i!=1:
        corr_var_list.append(i)
print(corr_var_list)

# Code ends here
# print(correlation)


# --------------
#Import libraries 
import numpy as np
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler

# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)

X =dataset.drop('Cover_Type', axis =1)
Y =dataset['Cover_Type'].copy()

# performing train-test split
X_train, X_test, Y_train, Y_test =cross_validation.train_test_split(X,Y, test_size =0.2, random_state =0)

# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.

size =10 # First 10 features for continuous data

#Standardized
#Apply transform only for continuous data
scaler =StandardScaler()
X_train_temp =scaler.fit_transform(X_train.iloc[:,0:size])
X_test_temp =scaler.transform(X_test.iloc[:,0:size])

#Concatenate scaled continuous data and categorical
X_train1 =np.concatenate((X_train_temp, X_train.iloc[:,size:]), axis=1)
X_test1 =np.concatenate((X_test_temp, X_test.iloc[:, size:]), axis=1)

# new dataframe for train and test data
scaled_features_train_df =pd.DataFrame(data =X_train1, index=X_train.index, columns=X_train.columns)
scaled_features_test_df =pd.DataFrame(data =X_test1, index=X_test.index, columns=X_test.columns)



# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif


# Write your solution here:

skb =SelectPercentile(score_func=f_classif, percentile=90)


# predictors
predictors =skb.fit_transform(X_train1, Y_train)

# scores
scores =skb.scores_.tolist()

# Features
Features =scaled_features_train_df.columns

# Dataframe of the features
dataframe =pd.DataFrame(list(zip(Features, scores)), columns=['Features','scores'])

dataframe.sort_values(by='scores', ascending=False, inplace=True)
#print(dataframe)

# Top k-predictors
top_k_predictors = list(dataframe['Features'][:predictors.shape[1]])
print(top_k_predictors)


# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score


# creating one vs rest classifier object
clf =OneVsRestClassifier(LogisticRegression())
clf1 =OneVsRestClassifier(LogisticRegression())

#model with all features
model_fit_all_features =clf1.fit(X_train, Y_train)
predictions_all_features =clf1.predict(X_test)

# accuracy of model with all features
score_all_features =accuracy_score(Y_test, predictions_all_features)
print(score_all_features)

# model with top k features
model_fit_top_features =clf.fit(scaled_features_train_df[top_k_predictors], Y_train)
predictions_top_features =clf.predict(scaled_features_test_df[top_k_predictors])

# accuracy of model with top_K_features
score_top_features =accuracy_score(Y_test, predictions_top_features)
print(score_top_features)



# --------------
#Importing header files

import pandas as pd
from sklearn.model_selection import train_test_split


# Code starts here

# reading the data
data =pd.read_csv(path)

# splitting into features and targets
X =data.drop(['customer.id', 'paid.back.loan'], axis =1)
y =data['paid.back.loan'].copy()

# splitting into train and test
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size =0.3, random_state =0)


# Code ends here


# --------------
#Importing header files
import matplotlib.pyplot as plt

# Code starts here

# value count of paid.back.loan
fully_paid =y_train.value_counts()

# plotting the bar graph
plt.title("Bar graph of paid back loan")
plt.bar(fully_paid.index, fully_paid)
plt.show()

# Code ends here


# --------------
#Importing header files
import numpy as np
from sklearn.preprocessing import LabelEncoder


# Code starts here

# removing % character from int.rate feature and converting to float
X_train['int.rate'] = X_train['int.rate'].str.replace("%","").astype(float)

# didviding by 100
X_train['int.rate'] =X_train['int.rate']/100

# performing the above operation on X_test
X_test['int.rate'] =X_test['int.rate'].str.replace('%','').astype(float)
X_test['int.rate'] =X_test['int.rate']/100

# seperating numerical and categorical features
num_df =X_train.select_dtypes(exclude=['object'])
cat_df =X_train.select_dtypes(include=['object'])


print(num_df.info())

print(cat_df.info())


# --------------
#Importing header files
import seaborn as sns


# Code starts here


# name of all numerical columns
cols =list(num_df.columns)

# creating figure and axes
fig, axes =plt.subplots(9,1, figsize=(10,50))

for i in range(0,9):
    sns.boxplot(x =y_train, y =num_df[cols[i]], ax =axes[i])

# Code ends here


# --------------
# Code starts here

# column names for categorical features
cols =list(cat_df.columns)

# figure with 4 axes
fig, axes =plt.subplots(2,2, figsize=(20,10))

for i in range(2):
    for j in range(2):
        # plotting a count plot
        sns.countplot(x =X_train[cols[i*2+j]], hue =y_train, ax =axes[i,j])

# Code ends here


# --------------
#Importing header files
from sklearn.tree import DecisionTreeClassifier

# Code starts here
# label encoder object
le =LabelEncoder()

# filling the nll values with NA
X_train.fillna('NA')
X_test.fillna('NA')

for i in cat_df.columns:
    X_train[i] =le.fit_transform(X_train[i])

    X_test[i] =le.transform(X_test[i])

# mapping yes, no to 1,0 in y_train, y_test
y_train =y_train.map({'Yes':1,'No':0})
y_test =y_test.map({'Yes':1, 'No':0})

# creating a decision tree classifier
model =DecisionTreeClassifier(random_state =0)

# fitting the model
model.fit(X_train, y_train)

# calculating score
acc =model.score(X_test, y_test)
print(acc)

# Code ends here


# --------------
#Importing header files
from sklearn.model_selection import GridSearchCV

#Parameter grid
parameter_grid = {'max_depth': np.arange(3,10), 'min_samples_leaf': range(10,50,10)}

# Code starts here

# decision tree classifier
model_2 =DecisionTreeClassifier()

# using GridSearchCV for pruning the tree
p_tree =GridSearchCV(estimator =model_2, param_grid =parameter_grid, cv=5)

# fitting on the data
p_tree.fit(X_train, y_train)

# accuracy of the model
acc_2 =p_tree.score(X_test, y_test)
print(acc_2)

# Code ends here


# --------------
#Importing header files

from io import StringIO
from sklearn.tree import export_graphviz
from sklearn import tree
from sklearn import metrics
from IPython.display import Image
import pydotplus

# Code starts here

# dots for graph visualization
dot_data =export_graphviz(p_tree.best_estimator_, out_file =None, feature_names =X.columns,
filled =True, class_names =['loan_paid_back_yes','loan_paid_back_no'])

# plotting the graph
graph_big =pydotplus.graph_from_dot_data(dot_data)

# show graph - do not delete/modify the code below this line
img_path = user_data_dir+'/file.png'
graph_big.write_png(img_path)

plt.figure(figsize=(20,15))
plt.imshow(plt.imread(img_path))
plt.axis('off')
plt.show() 

# Code ends here



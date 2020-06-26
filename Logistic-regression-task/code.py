# --------------
# import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# Code starts here

# Loading the data
df =pd.read_csv(path)

print(df.head())

# Splitting into features and target
X =df.iloc[:,:-1]
y =df['insuranceclaim']

# Splitting into train and test
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size =0.2, random_state =6)

# Code ends here


# --------------
import matplotlib.pyplot as plt


# Code starts here

# plotting boxplot for bmi
plt.boxplot(X_train['bmi'])
plt.title("BMI boxplots", size =15)

q_value =X_train['bmi'].quantile(0.95)
print(q_value)

# Value counts of y_train
print(y_train.value_counts())

# Code ends here


# --------------
# Code starts here

# Checking correlation among features
relation =X_train.corr()

print(relation)

# plotting pairplot on X_train
# plt.title("Correlation among features", size=20)
sns.pairplot(X_train)
plt.show()

# Code ends here


# --------------
import seaborn as sns
import matplotlib.pyplot as plt

# Code starts here

# Creating figure and axes
fig, axes =plt.subplots(2,2, figsize =(16,16))
cols =['children', 'sex', 'region','smoker']

# plotting countplot
for i in range(0,2):
    for j in range(0,2):
        col =cols[i*2 +j]
        sns.countplot(x =X_train[col], hue =y_train, ax=axes[i,j])
plt.show()
# Code ends here


# --------------
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# parameters for grid search
parameters = {'C':[0.1,0.5,1,5]}

# Code starts here

# Creating a LogisticRegression model
lr =LogisticRegression(random_state =9)

# Performing GridSearch on logistic model
grid =GridSearchCV(lr, param_grid= parameters)

# fitting the model on Training data
grid.fit(X_train, y_train)

# Predicting on the model
y_pred =grid.predict(X_test)

# Calculating accuracy for model
accuracy =accuracy_score(y_test, y_pred)

print(accuracy)

# Code ends here


# --------------
from sklearn.metrics import roc_auc_score
from sklearn import metrics

# Code starts here

# Calculating roc_auc score
score =roc_auc_score(y_test, y_pred)
print(score)

# Probability of X_test on model
y_pred_proba =grid.predict_proba(X_test)[:,1]

# calculating fpr and tpr
fpr, tpr, _ =metrics.roc_curve(y_test, y_pred)
print(fpr,tpr, _,end='\n')

# calculating roc_auc
roc_auc =roc_auc_score(y_test, y_pred_proba)
print(roc_auc)

# plotting ruc_auc 
plt.plot(fpr, tpr, label ="Logistic model, auc="+str(roc_auc))
plt.legend()

# Code ends here



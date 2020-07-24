# --------------
import pandas as pd
from sklearn.model_selection import train_test_split
#path - Path of file 

# Code starts here

# laoding the data
df =pd.read_csv(path)

# features and targets
X =df.drop(['customerID','Churn'], axis =1).copy()
y =df['Churn'].copy()

# performing traintestsplit
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size =0.3, random_state =0)




# --------------
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Code starts here

# cleaning X_train and X_test
X_train['TotalCharges'] =X_train['TotalCharges'].apply(lambda x: np.NaN if x==' ' else x)
X_test['TotalCharges'] =X_test['TotalCharges'].apply(lambda x: np.NaN if x==' ' else x)

# changing dtype of TotalCharges to float
X_train['TotalCharges'] =X_train['TotalCharges'].astype(float)
X_test['TotalCharges'] =X_test['TotalCharges'].astype(float)

# filling missing values with mean
X_train['TotalCharges'].fillna(np.mean(X_train['TotalCharges']), inplace =True)
X_test['TotalCharges'].fillna(np.mean(X_test['TotalCharges']), inplace =True)

# checking for null values in all other columns
print(X_train.isnull().sum())

# categorical columns list
cat_list =list(X_train.select_dtypes(include ='object'))

# initializing a LabelEncoder object
le =LabelEncoder()

for col in cat_list:
    X_train[col] =le.fit_transform(X_train[col])
    X_test[col] =le.transform(X_test[col])

# replacing 'No':0 and 'Yes':1
y_train =y_train.replace({'No':0,'Yes':1})
y_test =y_test.replace({'No':0,'Yes':1})



# --------------
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Code starts here

# observing the data
print(X_train.head())
print(X_test.head())
print(y_train.head())
print(y_test.head())

# intializing a AdaBoostClassifier()
ada_model =AdaBoostClassifier(random_state =0)

# training the model
ada_model.fit(X_train, y_train)

# predicting on the model
y_pred =ada_model.predict(X_test)

# accuracy_score of the model
ada_score =accuracy_score(y_test, y_pred)
print("Accuracy score of the model :%.2f"%ada_score)

# confusion matrix
ada_cm =confusion_matrix(y_test,y_pred)
print("Confusion Matrix :",ada_cm)

# classification report
ada_cr =classification_report(y_test, y_pred)
print(ada_cr)



# --------------
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

#Parameter list
parameters={'learning_rate':[0.1,0.15,0.2,0.25,0.3],
            'max_depth':range(1,3)}

# Code starts here

# initialising a XGBoost classifier
xgb_model =XGBClassifier(random_state =0)

# training the model
xgb_model.fit(X_train, y_train)

# prediciting on the model
y_pred =xgb_model.predict(X_test)

# accuracy_score between y_test and y_pred
xgb_score =accuracy_score(y_test, y_pred)
print("XGB Score : ",xgb_score)

# confusion_matrix matrix for XGBoost
xgb_cm =confusion_matrix(y_test, y_pred)
print("Confusion Matrix : /n",xgb_cm)

# classification_report
xgb_cr =classification_report(y_test, y_pred)
print("Classification Report /n",xgb_cr)

# performing hyper_parameter tuning

# GridSearch object
clf_model =GridSearchCV(estimator =xgb_model, param_grid =parameters)

# training the model
clf_model.fit(X_train, y_train)

# prediciting on the model
y_pred =clf_model.predict(X_test)

# accuracy_score between y_test and y_pred
clf_score =accuracy_score(y_test, y_pred)
print("XGB Score : ",clf_score)

# confusion_matrix matrix for XGBoost tuned
clf_cm =confusion_matrix(y_test, y_pred)
print("Confusion Matrix : /n",clf_cm)

# classification_report
clf_cr =classification_report(y_test, y_pred)
print("Classification Report /n",clf_cr)





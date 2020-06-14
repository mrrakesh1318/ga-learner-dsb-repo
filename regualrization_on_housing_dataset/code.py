# --------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# path- variable storing file path

# Loading dataset
df =pd.read_csv(path)

# Displaying top 5 values
print(df.head())

# Seperating features and targets into X and y
X =df.drop('Price', axis=1)

y =df['Price']

# Splitting into train and test
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size =0.3, random_state =6)

# Checking collinearity between features
corr =X_train.corr()
print(corr)


#Code starts here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Code starts here

# Linear Model Creation
regressor =LinearRegression()

# Fitting the model on training data
regressor.fit(X_train, y_train)

# Making predicitons on the data
y_pred =regressor.predict(X_test)

# Calculating R-squared 
r2 =r2_score(y_test, y_pred)

print(r2)


# --------------
from sklearn.linear_model import Lasso

# Code starts here

# Creating a lasso model
lasso =Lasso()

# Fitting on the model
lasso.fit(X_train, y_train)

# Making predictions on the model
lasso_pred =lasso.predict(X_test)

# Calcualting R-squared on lasso model
r2_lasso =r2_score(y_test, lasso_pred)

print("The R-sqaured with lasso model is {}".format(r2_lasso))


# --------------
from sklearn.linear_model import Ridge

# Code starts here

# Creating a ridge model object
ridge =Ridge()

# Fitting on the model
ridge.fit(X_train, y_train)

# Predicting on the model
ridge_pred =ridge.predict(X_test)

# Calculating R-sqaured
r2_ridge =r2_score(y_test, ridge_pred)

print(r2_ridge)
# Code ends here


# --------------
from sklearn.model_selection import cross_val_score

#Code starts here

# Creating a linear regression object
regressor =LinearRegression()

# Perfroming 10fold cross-validation
score =cross_val_score(regressor, X_train, y_train, cv=10)

mean_score =np.mean(score)

print(mean_score)




# --------------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#Code starts here

# Creating polynomial regression model
model =make_pipeline(PolynomialFeatures(2), LinearRegression())

# Fitting on the model
model.fit(X_train, y_train)

# Predicting on the model
y_pred =model.predict(X_test)

# Calculating R-squared
r2_poly =r2_score(y_test, y_pred)

print(r2_poly)



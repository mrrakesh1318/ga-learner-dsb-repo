# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here

# Loading dataset
df =pd.read_csv(path)

print(df.head())
#print(df.columns)

X =df[['ages', 'num_reviews', 'piece_count', 'play_star_rating',
       'review_difficulty', 'star_rating', 'theme_name', 'val_star_rating',
       'country']]
y =df['list_price']

X_train,X_test,y_train,y_test =train_test_split(X, y, test_size =0.3, random_state = 6)
# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols =X_train.columns

fig,axes =plt.subplots(3,3, sharey =True)

axes =axes.flatten()

df.plot( kind ="scatter",x='ages', y =1, ax =axes[0], figsize =(18,18))
df.plot( kind ="scatter",x='num_reviews', y =1,  ax =axes[1])
df.plot( kind ="scatter",x='piece_count', y =1, ax =axes[2])
df.plot( kind ="scatter",x='play_star_rating', y =1, ax =axes[3])
df.plot( kind ="scatter",x='review_difficulty', y =1 , ax =axes[4])
df.plot( kind ="scatter",x='star_rating', y =1, ax =axes[5])
df.plot( kind ="scatter",x='theme_name', y =1, ax =axes[6])
df.plot( kind ="scatter",x='val_star_rating', y =1, ax =axes[7])
df.plot( kind ="scatter",x='country', y =1, ax =axes[8])
# code ends here



# --------------
# Code starts here

# Calculating correlation between all features
corr =X_train.corr()
print(corr)

# Dropping features with correlation > (+/-)0.75
X_train.drop(['play_star_rating','val_star_rating'], axis=1, inplace=True)

X_test.drop(['play_star_rating','val_star_rating'], axis=1, inplace=True)


# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here

# Model creation
regressor =LinearRegression()

# Fitting the model
regressor.fit(X_train, y_train)

# Predicting on X_test
y_pred =regressor.predict(X_test)

# Calculating mean_sqaured and r-sqaured values
mse =mean_squared_error(y_test, y_pred)
print("Mean sqaured Erro is {}".format(mse))

r2 =r2_score(y_test, y_pred)
print("R-sqaured value is {}".format(r2))


# Code ends here


# --------------
# Code starts here

residual =y_test - y_pred

residual.plot(kind ="hist")

# Code ends here



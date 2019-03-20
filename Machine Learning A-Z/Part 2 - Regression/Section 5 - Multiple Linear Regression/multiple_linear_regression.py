# Multiple linear regression

# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding the categorical variable
# Encoding independednt variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# LabelEncoder - Change text into numbers 
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
# OneHotEncoder - Different factors in categorical variable becomes features
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the dummy variable trap
X = X[:, 1:]

# Splitting the dataset into training and testing set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple regression model to training set
from sklearn.linear_model import LinearRegression
# Creating an object of the class
regressor = LinearRegression()
# Fit the object to our training set
regressor.fit(X_train, y_train)

# Predicting the test set
y_pred = regressor.predict(X_test)

# Building an optimal model using Backward Elimination
import statsmodel.formula.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)




















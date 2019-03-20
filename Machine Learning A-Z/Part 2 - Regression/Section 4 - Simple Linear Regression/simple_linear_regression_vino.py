# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:19:40 2018

@author: vino
"""

# Simple Linear Regression

# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importng the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into training and testing set
from sklearn.cross_validation import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting simple linear regression to training set #
from sklearn.linear_model import LinearRegression
# LinearRegression is a class and we are creating an object for that class
# LinearRegression() a function that will return object of itself
regressor = LinearRegression()
# Fit is a method of LinearRegression class 
# that would fit the simple linear regressor object to the training set
regressor.fit(X_train, y_train)
# By doing this the model will learn the correlations between salary and years of experience
# and it would learn how it can predict dependent variable (Salary) based on independent variable(Years of experience)

# Predicting the Test set results
# ypred - vector of predictions of dependent variable(Salary)
# To predict we use predict function from the LinearRegression class
ypred = regressor.predict(X_test)
 
# Visualising the training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Simple Linear Regression (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

















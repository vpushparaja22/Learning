# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:59:27 2018

@author: vinothini pushparaja
"""

# NUMPY

import numpy as np

"""
# create a 1d array from list which is the common ways to create an array
# The key difference between an array and a python list is, 
# arrays are designed to handle vectorized operations while a python list is not.

"""

list1 = [0,1,2,3,4]
arr1d = np.array(list1)

# print the array and its type
print(type(arr1d))
print(arr1d)

# That means, if you apply a function it is performed on every item in the array, 
# rather than on the whole array object.

# Let's say we want to add 2 to every iteam in the list.
# The best way to do it like the one below, but it will not work for python list
list1 + 2
# But you can do that in an ndarray
arr1d + 2

"""
# Another characteristic is that, once a numpy array is created, 
# you cannot increase its size. To do so, you will have to create a new array. 
# But such a behavior of extending the size is natural in a list.
# Nevertheless, there are so many more advantages. Let’s find out.
"""
# So, that’s about 1d array. You can also pass a list of lists to create a matrix like a 2d array

# create a 2d array from a list of lists
list2 = [[0,1,2],[3,4,5],[6,7,8]]
arr2d = np.array(list2)

print(arr2d)

# create a float 2d array
arr2d_f = np.array(list2, dtype=float)
print(arr2d_f)

# You can also convert it to a different datatype using the %astype% method.
arr2d_f.astype('int')

# convert to int and then to str datatype
arr2d_f.astype('int').astype('str')

## A numpy array must have all items to be of the same data type, unlike lists. 
## This is another significant difference.

"""
# However, if you are uncertain about what datatype your array will hold or if you want to 
# hold characters and numbers in the same array, you can set the dtype as 'object'.
"""

arr1d_b = np.array([1,0,10], dtype=bool)
arr1d_b

arr1d_o = np.array([1, 'vino'], dtype=object)
arr1d_o

# Finally, you can always convert an array back to a python list using tolist().
arr1d_o.tolist()

"""
1. Arrays support vectorised operations, while lists don’t.
2. Once an array is created, you cannot change its size. 
   You will have to create a new array or overwrite the existing one.
3. Every array has one and only one dtype. All items in it should be of that dtype.
4. An equivalent numpy array occupies much less space than a python list of lists.
"""

# Every array has some properties I want to understand in order to know about the array.

"""
Well I want to know about the array that I didn't create:
    
1. If it is a 1D or a 2D array or more. (ndim)

2. How many items are present in each dimension (shape)

3. What is its datatype (dtype)

4. What is the total number of items in it (size)

5. Samples of first few items in the array (through indexing)
"""

# create a 2d array with 3 rows and 4 columns
list2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
arr2 = np.array(list2, dtype = float)
arr2

# shape
print("Array shape: ", arr2.shape)

# dtype
print("Array Data type: ", arr2.dtype)

# size
print("Array size or no. of iteams present: ", arr2.size)

#num of dimensions
print("Num of dimensions: ", arr2.ndim)

###
# Extract specific items from array
###

# below extracts first 2 rows (0,1) and columns (0,1)
# But unlike lists, numpy arrays can optionally accept as many parameters 
# in the square brackets as there is number of dimensions.
arr2[:2,:2]
# this produces error
list2[:2,:2]

# A boolean index array is of the same shape as the array-to-be-filtered and it contains only 
# True and False values. The values corresponding to True positions are retained in the output.

b = arr2 > 4
b

# get the items from the array that are greater than 4
arr2[b]

##
# Reverse the rows and the whole array
##

# reverse only the row position
arr2[::-1,]
# reverse the rows first and then the column
arr2[::-1, ::-1]

arr2[::-1].sort(axis=1)
# To transpose an array either use this
np.transpose(arr2)

# or use
arr2.T

##
# How to represent missing values and infinite?
##

# Missing values can be represented using %np.nan% object, while %np.inf% represents infinite.

# Insert a nan and inf
arr2[2,2] = np.nan # not a number
arr2[1,0] = np.inf # infinite

arr2

# Replace nan and inf with -1. Don't use arr2 == np.nan
missing_bool = np.isnan(arr2) | np.isinf(arr2)
arr2[missing_bool] = -1
arr2

##
# Compute mean, min, max on the ndarray
##

# For the whole array
print("Mean: ", arr2.mean())
print("Min: ", arr2.min())
print("Max: ", arr2.max())

# To compute minimum values column wise or row wise use np.amin
print("Column wise minimum: ", np.amin(arr2, axis=0))
print("Row wise minimum: ", np.amin(arr2, axis=1))

# Computing the minimum row-wise is fine. But what if you want to do some other 
# computation/function row-wise? It can be done using the %np.apply_over_axis% 
# which you will see in the upcoming topic.
arr2
np.cumsum(arr2)

##
# Create a new array from the existing array
##

# If you just assign a portion of array to a new array, the new array refers to the parent array.
# This means if any changes made in the new array it will get reflected in the parent array
# That is why we need to use copy() if we need a copy of an array

arr2a = arr2[:2, :2]
arr2a[1,1] = 100

arr2a
arr2

arr2b = arr2[:2,:2].copy()
arr2b[1,1] = 200

arr2b
arr2

###
# Reshaping and Flattening Multidimensional arrays
###

# Reshape a 3x4 array into 4x3
arr2.reshape(4,3)

# Setting to -1 it automatically decides the number of columns
arr2.reshape(4, -1)

# There are 2 ways to flatten an array using flatten() and ravel()

# The difference between ravel and flatten is, the new array created using ravel is actually a
# reference to the parent array. So, any changes to the new array will affect the parent as well.
# But is memory efficient since it does not create a copy

# Flatten it to a 1d array
arr2.flatten()

# changing the flattened array does not change the parent array
b1 = arr2.flatten()
b1[0] = 100 # changing b1 does not affect arr2
b1
arr2

# changing the ravel array does change the parent array
b2 = arr2.ravel()
b2[0] = 101
b2
arr2

###
# Create Sequences repetitions and random numbers using numpy
###

# np.arange() comes handy when to create customised number sequences

# lower limit is 0 by default
print(np.arange(5))

# 0 to 9
print(np.arange(0, 10))

# 0 to 9 with step of 2
print(np.arange(0, 9, 2))

# 10 to 1 in decreasing order
print(np.arange(10, 0, -1))

"""
# You can set the starting and end positions using np.arange. 
# But if you are focussed on the number of items in the array you will have to manually 
# calculate the appropriate step value.

# Say, you want to create an array of exactly 10 numbers between 1 and 50, 
# Can you compute what would be the step value?

Well, I am going to use the np.linspace instead.
"""

# Start at 1 end at 50
np.linspace(start=1, stop=50, num=10, dtype=int)

"""
Similar to %np.linspace%, there is also %np.logspace% which rises in a logarithmic scale. 
In np.logspace, the given start value is actually base^start and ends with base^stop, 
with a default based value of 10.
"""

# Limit the number of digits after decimal point to 2
np.set_printoptions(precision=2)

# Start at 10^1 and end at 10^50
np.logspace(start=1, stop=50, num=10, base=10)

"""
np.zeros(arr) --> Creates an array of desired shape where all the items are 0
np.ones(arr) --> Creates an array of desired shape where all the items are 1
"""

np.zeros([2,2], dtype=int)

np.ones([2,2], dtype=int)

###
# Create repeating sequences
###

"""
np.tile(arr, no_of_repetition) --> repeata a whole list of array n times
np.repeat(arr, no_of_repetition) --> repeats each item in an array n times
"""

a = [1,2,3]

# Repeat whole of a two times
print("Tile: ", np.tile(a,2))

# Repeat each element of a two times
print("Repeat: ", np.repeat(a,2))

###
# Generate Random Numbers
###

"""
The %random% module provides nice functions to generate random numbers 
(and also statistical distributions) of any given shape.
"""

# Random numbers between [0,1] of shape 2,2
print(np.random.rand(2,2))

# Normal distribution with mean=0 and variance=1 of shape 2,2
print(np.random.randn(2,2))

# Random integers between (0,10) of shape 2,2
print(np.random.randint(0, 10, size=[2,2]))

# One random number between 0 and 1
print(np.random.random())

# Random numbers between (0,1) of shape 2,2
print(np.random.random(size=[2,2]))

# Pick 10 items from a given list, with equal probability
print(np.random.choice(['a','e','i','o','u'], size=10))

# Pick 10 items from a given list with a predefined probability 'p'
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10, p=[0.3, .1, 0.1, 0.4, 0.1]))
# picks more o's

# Create a random state
rn = np.random.RandomState(100)

# Create random number between 0 and 1
print(rn.rand(2,2))
print(rn.randn(2,2))
print(rn.randint(0, 10, size=(2,2)))



# Set the random seed
np.random.seed(100)

# Create random numbers between 0 and 1
np.random.rand(2,2)
np.random.randn(2,2)
np.random.randint(0, 10, size=(2,2))


###
# Get the unique items and the counts
###

"""
unique, count = np.unique(arr, return_counts=False) --> used to get the unique items.
If you want the repetition counts of each item, set the return_counts parameter to True.
"""

arr_rand = np.random.randint(0, 10, size = 10)
arr_rand

uniq, counts = np.unique(arr_rand, return_counts=True)
print("Unique: "+ str(uniq) + "\n Count: " + str(counts))

































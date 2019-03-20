# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:49:34 2019

@author: vinothini pushparaja
"""

import numpy as np

"""
np.where(condition, '1', '0') --> locates the positions in the array where a given condition 
                                holds true, If true the prints 1 else if its false it prints 0.
arr.take(index) --> take items from the given index position
"""

arr_rand = np.array([8, 8, 3, 7, 7, 0, 4, 2, 5, 2])
print('Array: ', arr_rand)

# Positions where value greater than 5
index_gt5 = np.where(arr_rand>5)
print('Positions where value > 5: ', index_gt5)

# Take items at given index
get_item = arr_rand.take(index_gt5)
print('Take items from arr_rand for the given index: ', get_item)

# np.where also accepts 2 more optional arguments x and y. 
# Whenever condition is true, ‘x’ is yielded else ‘y’.

# If value > 5 then prints gt5 else lt5
np.where(arr_rand > 5, 'gt5', 'lt5')

"""
np.argmax(arr) --> finds the position/location of maximum value in an array
np.argmin(arr) --> finds the position/location of minimum value in an array
"""

print("Position of maximum value in arr_rand: ", np.argmax(arr_rand))
print("Position of minimum value in arr_rand: ", np.argmin(arr_rand))

"""
np.genfromtext(path) --> import datasets from web URLs, handle missing values, multiple delimiter
                         handle irregular number of columns etc. 
np.loadtxt() --> which assumes the dataset has no missing values

Eg: Since all elements in a numpy array should be of the same data type, 
    the last column which is a text will be imported as a ‘nan’ by default.
"""

# Turn off scientific notation
np.set_printoptions(suppress=True)

# Import data form csv file url
path = 'https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv'
data = np.genfromtxt(path, delimiter=',', skip_header=1, filling_values=-999, dtype='float')

data[:3] # First 3 rows

##############
# did you notice all the values in last column has the same value ‘-999’?
# That happened because, I had mentioned the. `dtype=’float’`. 
# The last column in the file contained text values and since all the values in a 
# numpy array has to be of the same `dtype`, `np.genfromtxt` didn’t know how to 
# convert it to a float.
##############

"""
In case, you MUST have the text column as it is without replacing it with a placeholder, 
you can either set the dtype as ‘object’ or as None.
"""

data2 = np.genfromtxt(path, delimiter=',', skip_header=1, dtype=object)

### OR

data2 = np.genfromtxt(path, delimiter=',', skip_header=1, dtype=None)

data2[:3]


"""
np.savetxt() -->  export the array as a csv file.
"""

np.savetxt('out.csv', data, delimiter=',')

"""
At some point, we will want to save large transformed numpy arrays to disk and 
load it back to console directly without having the re-run the data transformations code.
Numpy provides the .npy and the .npz file types for this purpose.

np.save('file name', arr) --> If you want to store a single ndarray object, 
                                store it as a .npy file using np.save
                                
np.savez('file name', arr1, arr2) --> If you want to store more than 1 ndarray object in a 
                                    single file, then save it as a .npz file using np.savez.
                                    
np.load() --> Can load back the .npy and .npz file using np.load()
"""

# save a single numpy array object as .npy
np.save('myarray.npy', arr_rand)

# save multiple numpy array object in a .npz file
np.savez('myarray2.npz', arr_rand, arr_rand)

# load the .npy file
a = np.load('myarray.npy')
print(a)

# load .npz file
b = np.load('myarray2.npz')
print(b.files)
b['arr_0']

"""
3 different ways of concatenating two or more numpy arrays.

    Method 1: np.concatenate() by changing the axis parameter to 0 and 1
    Method 2: np.vstack() and np.hstack()
    Method 3: np.r_() and np.c_()
    
"""

a = np.zeros([4,4])
b = np.ones([4,4])

print(a)
print(b)

# Vertical array stacking
print(np.concatenate([a,b], axis=0))
print(np.vstack([a,b]))
print(np.r_[a,b])

# Horizontal array stacking
print(np.concatenate([a,b], axis=1))
print(np.hstack([a,b]))
print(np.c_[a,b])

# Besides, you can use np.r_ to create more complex number sequences in 1d arrays.
print(np.r_[[1,2,3],0,0,3,[5,6,7]])

"""
SORT
np.sort() --> np.sort function with axis=0, all the columns will be sorted in ascending order 
            independent of eachother, effectively compromising the integrity of the row items. 
            In simple terms, the values in each row gets corrupted with values from other rows.
"""

arr = np.random.randint(1,6, size=[8,4])
print(arr)

np.sort(arr, axis=0)

##
# I don’t want the content of rows to be disturbed, I resort to an indirect method using 
# np.argsort.
##

"""
np.argsort() --> returns the index positions of an array, use that to sort the array. See below
            
"""
# In array ‘x’, the 0th item is the smallest, 3rd item is the second smallest and so on.
x = np.array([2,9,5,6,1,8])
sort_index = np.argsort(x)
print(sort_index)

x[sort_index]

# Now, in order to sort the original arr, I am going to do an argsort on the 1st column 
# and use the resulting index positions to sort arr.
# argsort the first column
sorted_indx_1stcol = arr[:,0].argsort()

# Sort 'arr' by first column without disturbing the integrity of rows
print(arr[sorted_indx_1stcol])
print(arr)

# sort in descending order simple reverse the srsorted index

print(arr[sorted_indx_1stcol[::-1]])


"""
np.lexsort() --> sort a numpy array based on 2 or more columns.
        pass a tuple of columns based on which the array should be sorted.
        Remember to place the column to be sorted first at the rightmost side inside the tuple.
"""
tuple_arr = ((arr[:,1], arr[:,0]))
lex_sorted = np.lexsort(tuple_arr)

print(arr[lex_sorted])





































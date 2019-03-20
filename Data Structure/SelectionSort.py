# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:03:28 2019

@author: vino2
"""

"""
repeat (numOfElements - 1) times

  set the first unsorted element as the minimum

  for each of the unsorted elements

    if element < currentMinimum

      set element as new minimum

  swap minimum with first unsorted position
"""

def selectionSort(l):
    count = 0
    while count < len(l):
        min = l[count]
        index = 0
        for j in range(count,len(l)):
            if l[j] <= min:
                min = l[j]
                index = j
        temp = l[count]
        l[count] = min
        l[index] = temp
        count += 1
    return l
        
list = selectionSort([4,7,2,3,1,9,40,38,20,4,35])
print(list)

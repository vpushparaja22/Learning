# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:10:53 2019

@author: vino2
"""

"""
Pseudocode:
    do

      swapped = false

      for i = 1 to indexOfLastUnsortedElement-1

        if leftElement > rightElement

          swap(leftElement, rightElement)

          swapped = true; swapCounter++

    while swapped
"""

def bubbleSort(list1):
    count = 0
    while count < len(list1):
        for i in range(0, len(list1)-1):
            if list1[i] > list1[i+1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp
        count += 1
    return list1
l = bubbleSort([9,3,6,8,2])
print(l)
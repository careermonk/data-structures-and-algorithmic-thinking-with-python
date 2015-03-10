# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import random
def QuickSort(A, low, high):
    if low < high:
        pivot = Partition(A, low, high)
        QuickSort(A, low, pivot - 1)
        QuickSort(A, pivot + 1, high)
 
def Partition(A, low, high) :
    pivot = low + random.randrange(high - low + 1)
    swap(A, pivot, high)
    for i in range(low, high):
        if A[i] <= A[high]:
            swap(A, i, low)
            low += 1
 
    swap(A, low, high)
    return low
 
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
QuickSort(A, 0, len(A) - 1)
print(A)

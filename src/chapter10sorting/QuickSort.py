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
def QuickSort(A, first, last):
    if first < last:
        pivot = Partition(A, first, last)
        QuickSort(A, first, pivot - 1)
        QuickSort(A, pivot + 1, last)
 
def Partition(A, first, last) :
    pivot = first + random.randrange(last - first + 1)
    swap(A, pivot, last)
    for i in range(first, last):
        if A[i] <= A[last]:
            swap(A, i, first)
            first += 1
 
    swap(A, first, last)
    return first
 
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
QuickSort(A, 0, len(A) - 1)
print(A)

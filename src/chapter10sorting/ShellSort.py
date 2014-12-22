# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def ShellSort(A):
    sublistcount = len(A) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(A, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", A)
        sublistcount = sublistcount // 2

def gapInsertionSort(A, start, gap):
    for i in range(start + gap, len(A), gap):
        currentvalue = A[i]
        position = i
        while position >= gap and A[position - gap] > currentvalue:
            A[position] = A[position - gap]
            position = position - gap

        A[position] = currentvalue

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
ShellSort(A)
print(A)

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				           warranty; without even the implied warranty of 
# 				            merchantability or fitness for a particular purpose. 

def sortedSquaredArray(A):
    n = len(A)
    j = 0
    # Find the last index of the negative numbers
    while j <n and A[j] < 0:
        j += 1
    # i points to the last index of negative numbers
    i = j-1
    result = []
    # j points to the first index of the positive numbers
    while i >= 0 and j < n:
        if A[i]**2 < A[j]**2:
            result.append(A[i]**2)
            i -= 1
        else:
            result.append(A[j]**2)
            j += 1

    # add the remaining negative numbers squares to result
    while i>= 0:
        result.append(A[i]**2)
        i -= 1

    # add the remaining positive numbers squares to result
    while j < n:
        result.append(A[j]**2)
        j += 1

    return result

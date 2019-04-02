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
    result = []
    for i in range(len(A)):
        result.append(A[i]*A[i])
  result.sort()
    return result

A = [-6, -4, 1, 2, 3, 5]
print sortedSquaredArray(A)

#Second approach
def sortedSquaredArray(A):
    return sorted([i**2 for i in A])

A = [-6, -4, 1, 2, 3, 5]
print sortedSquaredArray(A)

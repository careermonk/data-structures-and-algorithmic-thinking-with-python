# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findInRotatedSortedArrayWithRecursion(A, target):
	if A == None or len(A) == 0:
	    return -1;
	low = 0;
	high = len(A) - 1
	return findWithRecursion(A, target, low, high)

def findWithRecursion(A, target, low, high):
	if low > high:
	    return -1
	mid = (low + high) / 2

	if A[mid] == target:
	    return mid
	if A[low] < A[mid]:
	    if A[low] <= target < A[mid]:
		return findWithRecursion(A, target, low, mid - 1)
	    return findWithRecursion(A, target, mid + 1, high)
	elif A[low] > A[mid]:
	    if A[mid] < target <= A[high]:
		return findWithRecursion(A, target, mid + 1, high)
	    return findWithRecursion(A, target, low, mid - 1)
	else:
	    if A[mid] != A[high]:
		return findWithRecursion(A, target, mid + 1, high)
	    result = findWithRecursion(A, target, low, mid - 1)
	    if result != -1:
		return result
	    return findWithRecursion(A, target, mid + 1, high)
	    
A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]		
print findInRotatedSortedArrayWithRecursion(A, 5)	    

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findInRotatedSortedArray(A, target):
	left = 0
	right = len(A) - 1
	while left <= right:
	    mid = (left + right) / 2
	    if A[mid] == target:
		return mid
	    if A[mid] >= A[left]:
		if A[left] <= target < A[mid]:
		    right = mid - 1
		else:
		    left = mid + 1
	    else:
		if A[mid] < target <= A[right]:
		    left = mid + 1
		else:
		    right = mid - 1
	return -1
	
A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]		

print findInRotatedSortedArray(A, 5)

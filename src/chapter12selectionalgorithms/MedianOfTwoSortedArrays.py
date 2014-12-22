# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findKthSmallest(A, B, k):
    if len(A) > len(B):             A, B = B, A
    # stepsA = (endIndex + beginIndex_as_0) / 2
    stepsA = (min(len(A), k) - 1) / 2
    # stepsB =  k - (stepsA + 1) -1 for the 0-based index
    stepsB = k - stepsA - 2

    # Only array B contains elements
    if len(A) == 0:                 return B[k - 1]
    # Both A and B contain elements, and we need the smallest one
    elif k == 1:                    return min(A[0], B[0])
    # The median would be either A[stepsA] or B[stepsB], while A[stepsA] and 
    # B[stepsB] have the same value.
    elif A[stepsA] == B[stepsB]:    return A[stepsA]
    # The median must be in the right part of B or left part of A
    elif A[stepsA] > B[stepsB]:     return findKthSmallest(A, B[stepsB + 1:], k - stepsB - 1)
    # The median must be in the right part of A or left part of B
    else: return findKthSmallest(A[stepsA + 1:], B, k - stepsA - 1)

    
def findMedianSortedArrays(A, B):    
	# There must be at least one element in these two arrays
	assert not(len(A) == 0 and len(B) == 0)

	if (len(A) + len(B)) % 2 == 1:
	    # There are odd number of elements in total. The median the one in the middle
	    return findKthSmallest(A, B, (len(A) + len(B)) / 2 + 1) * 1.0
	else:
	    # There are even number of elements in total. The median the mean value of the
	    # middle two elements.
	    return (findKthSmallest(A, B, (len(A) + len(B)) / 2 + 1) + \
		     findKthSmallest(A, B, (len(A) + len(B)) / 2)) / 2.0
	
A = [127, 220, 246, 277, 321, 454, 534, 565, 933]
B = [12, 22, 24, 27, 32, 45, 53, 65, 93]	
	
print(findMedianSortedArrays(A, B))

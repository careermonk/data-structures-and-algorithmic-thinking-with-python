# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findMinimumInRotatedSortedArray(A):
        mid, low, high = 0, 0, len(A) - 1
        while A[low] >= A[high]:
            if high - low <= 1:
                return A[high], high
            mid = (low + high) >> 1
            if A[mid] == A[low]:
                low += 1
            elif A[mid] > A[low]:
                low = mid
            elif A[mid] == A[high]:
                high -= 1
            else:
                high = mid
        return A[low], low

A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]	
print findMinimumInRotatedSortedArray(A)

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def binarySearchLastOccurrence(A, target):
	if A == None or len(A) == 0:
	    return -1;
	high = len(A) - 1
        low = 0
        m = 0
        lastFound = -1;
        while(1):
            if (low > high): return lastFound
            m = (low + high) / 2
            if (A[m] == target):
		    lastFound = m; low = m + 1
            if (A[m] < target): low = m + 1
            if (A[m] > target): high = m - 1

        return m
	    
A = [5, 6, 9, 12, 15, 21, 21, 34, 45, 57, 70, 84]		
print binarySearchLastOccurrence(A, 21)

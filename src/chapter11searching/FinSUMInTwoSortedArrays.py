# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def BinarySearchIterative(numbersList, value):
    low = 0
    high = len(numbersList) - 1
    while low <= high: 
        mid = (low + high) // 2
        if numbersList[mid] > value: high = mid - 1
        elif numbersList[mid] < value: low = mid + 1
        else: return mid
    return -1
		
def findSumInLists(A, B, k):
	A.sort()
	for i in range(0, len(B)):
		c = k - B[i] 	
		if(BinarySearchIterative(A, c) != -1):
			return 1
	return 0	

		
A = [2, 3, 5, 7, 12, 15, 23, 32, 42]
B = [3, 13, 13, 15, 22, 33]
print findSumInLists(A, B, 270)

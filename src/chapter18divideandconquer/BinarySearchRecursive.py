# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def BinarySearchRecursive(numbersList, value, low=0, high=-1):
    if not numbersList: return -1
    if(high == -1): high = len(numbersList) - 1
    if low == high:
        if numbersList[low] == value: return low
        else: return -1
    mid = low + (high - low) // 2
    if numbersList[mid] > value: return BinarySearchRecursive(numbersList, value, low, mid - 1)
    elif numbersList[mid] < value: return BinarySearchRecursive(numbersList, value, mid + 1, high)
    else: return mid
	    
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(BinarySearchRecursive(A, 277))    

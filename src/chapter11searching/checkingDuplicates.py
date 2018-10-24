# Copyright (c) Oct 22, 2018 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

from collections import defaultdict
##Explain the logic
def checkDuplicates(A):
	c = 0
	# If array length is 0 or not valid
	if (len(A)==0):
		return False
	for i in range(len(A)):
		for j in range(i+1, len(A)):
			c += 1
			if (A[i] == A[j]):
				print c
				return True
	print c
	return False
 
def checkDuplicates2(A):
	c = 0
	# If array length is 0 or not valid
	if (len(A)==0):
		return False
	for i in range(len(A)):
		for j in range(0, len(A)):
			c += 1
			if (i ==j):
				continue
			if (A[i] == A[j]):
				print c
				return True
	print c
	return False
 
def checkDuplicates3(A):
	c = 0
	# If array length is 0 or not valid
	if (len(A)==0):
		return False
 
	# Sorting the array elements
	A.sort()
	for i in range(len(A)):
		c += 1
		if (A[i] == A[i+1]):
			print c
			return True
	print c
	return False
 
def checkDuplicates4(A):
	h = defaultdict(int) # default value of int is 0
	for element in A:
		if (h[element] == 1):
			print h.items()
			return True
		else:
			h[element] = 1
	return False
 
def checkDuplicates5(A):
	# Error checks
	minimum = min(A)
	maximum = max(A)
	if minimum < 0 or maximum >= len(A):
		print("Not a avalid input")
		return False
	for i in range(len(A)):
		if(A[abs(A[i])] < 0):
			return True
		else:
			A[abs(A[i])] = -A[abs(A[i])]
 
	print("No duplicates in given array.")
	return False
 
#print checkDuplicates5([1,2,3,4,5,6,7,6])
#print checkDuplicates5([0,1,2,3,4,5,6])
#print checkDuplicates5([3,2,1,2,2,3])
print checkDuplicates5([3,2,1,2,2,-3])
 

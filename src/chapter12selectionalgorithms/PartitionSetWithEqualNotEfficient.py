# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# A utility function that returns 1 if there is a subset of A[] with sum equal to given sum
def subsetSum (A, n, sum):
	if (sum == 0): 
		return 1
	if (n == 0 and sum != 0):
		return 0
	# If last element is greater than sum, then ignore it
	if (A[n - 1] > sum):
		return subsetSum (A, n - 1, sum)

	return subsetSum (A, n - 1, sum) or subsetSum (A, n - 1, sum - A[n - 1])

 
# Returns 1 if A[] can be partitioned in two subsets of equal sum, otherwise 0
def findPartition(A):
	# calculate sum of all elements
	sum = 0
	n = len(A)
	for i in range(0, n):
		sum += A[i]

	# If sum is odd, there cannot be two subsets with equal sum
	if (sum % 2 != 0):
		return 0

	# Find if there is subset with sum equal to half of total sum
	return subsetSum (A, n, sum / 2)



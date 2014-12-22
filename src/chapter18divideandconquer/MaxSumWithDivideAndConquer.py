# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def maxSumWithDivideAndConquer(A, low, hi):
	# run MCS algorithm on condensed list
	if low is hi:
		return (low, low, A[low][2])
	else:
		pivot = (low + hi) / 2
		# max subsequence exclusively in left half
		left = maxSumWithDivideAndConquer(A, low, pivot)
		# max subsequence exclusively in right half
		right = maxSub(A, pivot + 1, hi)
		# calculate max sequence left from mid
		leftSum = A[pivot][2]
		temp = 0
		for i in xrange(pivot, low - 1, -1):
			temp += A[i][2]
			if temp >= leftSum:
				l = i
				leftSum = temp
		# calculate max sequence right from mid
		rightSum = A[pivot + 1][2]
		temp = 0
		for i in xrange(pivot + 1, hi + 1):
			temp += A[i][2]
			if temp >= rightSum:
				r = i
				rightSum = temp
		# combine to find max subsequence crossing mid
		mid = (l, r, leftSum + rightSum)
		if left[2] > mid[2] and left[2] > right[2]:
			return left
		elif right[2] > mid[2] and right[2] > left[2]:
			return right
		else:
			return mid
			
list = [100, -4, -3, -10, -5, -1, -2, -2, -0, -15, -3, -5, -2, 70]	

print maxSumWithDivideAndConquer(list, 0, len(list) - 1)

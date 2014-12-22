# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def threeElementsWithSumKWithSorting(A, K):
	n = len(A)
	left = 0
	right = n - 1
	for i in range(0, n - 2):
		left = i + 1
		right = n - 1
		while(left < right):
			print A[i] + A[left] + A[right], K
			if(A[i] + A[left] + A[right] == K):
				print "yes-->", A[i], " + ", A[left], " + ", A[right], " = ", K		
				return 1
			elif(A[i] + A[left] + A[right] < K):
				left += 1
			else:
				right -= 1
	return 0
    
A = [1, 6, 45, 4, 10, 18]
A.sort()
print threeElementsWithSumKWithSorting(A, 23)

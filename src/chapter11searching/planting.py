# Copyright (c) Oct 22, 2018 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def planting(A, K):
	counter = 0
	for i in range(0,len(A)):
		if (A[i] == 0 and (i == 0 or A[i-1] ==0) and ( i == len(A)-1 or A[i+1] == 0)):
			A[i] = 1
			counter += 1
			if counter == K:
				return True, A
	return False

print planting([1,0,0,0,1,0,0], 2)
print planting([1,0,0,0,1,0,0], 3)

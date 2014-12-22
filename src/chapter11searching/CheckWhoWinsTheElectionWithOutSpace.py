# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def CheckWhoWinsTheElection(A):
	A.sort()
	counter = maxCounter = 0
	candidate = maxCandidate = 0
	
	for i in range(0, len(A)):
		if(A[i] == candidate):
			counter += 1
		else:
			counter = 1
			candidate = A[i]

		if(counter > maxCounter):
			maxCandidate = A[i]
			maxCounter = counter

	print maxCandidate, "appeared ", maxCounter, " times"

		
A = [2, 3, 2, 1, 2, 2, 3, 2, 2]
CheckWhoWinsTheElection(A)
A = [3, 3, 3, 2, 2, 3]
CheckWhoWinsTheElection(A)

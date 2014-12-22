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
	counter = maxCounter = 0
	candidate = A[0]
	for i in range(0, len(A)):
		counter = 1
		for j in range(i + 1, len(A)):
			if(A[i] == A[j]): 
				counter += 1		
		if(counter > maxCounter):
			maxCounter = counter
			candidate = A[i]	
	print candidate, "appeared ", maxCounter, " times"

A = [3, 2, 1, 2, 2, 3]
CheckWhoWinsTheElection(A)
A = [3, 3, 3, 2, 2, 3]
CheckWhoWinsTheElection(A)

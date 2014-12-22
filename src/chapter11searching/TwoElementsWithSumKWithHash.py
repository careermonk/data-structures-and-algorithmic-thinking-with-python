# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def twoElementsWithSumKWithHash(A, K):
	table = {}  # hash
	for element in A:
		if element in table:
			table[element] += 1
		elif element != " ":
			table[element] = 1
		else:
			table[element] = 0			
	for element in A:
		if K - element in table:
			print "yes-->", element, "+", K - element, " = ", K			
A = [1, 4, 45, 6, 10, -8]
A.sort()
twoElementsWithSumKWithHash(A, 11)

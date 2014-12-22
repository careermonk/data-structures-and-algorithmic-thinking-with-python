# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def PrintTwoRepeatedElementsHash(A):
	table = {}  # hash
	for element in A:
		if element in table:
			table[element] += 1
		elif element != " ":
			table[element] = 1
		else:
			table[element] = 0

	for element in A:
		if table[element] == 2:
			print element
			
A = [3, 5, 7, 4, 2, 4, 2, 1, 9]
PrintTwoRepeatedElementsHash(A)

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def FirstRepeatedElementAmongRepeatedElementsWithHash(A):
	table = {}  # hash
	max = 0
	for element in A:
		if element in table and table[element] == 1:
			table[element] = -2
		elif element in table and table[element] < 0:
			table[element] -= 1			
		elif element != " ":
			table[element] = 1
		else:
			table[element] = 0

	for element in A:
		if table[element] < max:
			max = table[element]
			maxRepeatedElement = element

	print maxRepeatedElement, "repeated for ", abs(max), " times"
 
A = [3, 2, 1, 1, 2, 1, 2, 5, 5]
FirstRepeatedElementAmongRepeatedElementsWithHash(A)

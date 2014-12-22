# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def firstRepeatedChar(A):
	table = {}  # hash
	for char in A.lower():
		if char in table:
			table[char] += 1
			print("the first repeated character is: %s" % (char))
			return char
		elif char != " ":
			table[char] = 1
		else:
			table[char] = 0
	return

print firstRepeatedChar("careermonk")

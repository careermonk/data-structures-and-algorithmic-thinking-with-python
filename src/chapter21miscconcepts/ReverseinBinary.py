# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def reverse_number(n):
	nReverse = n
	s = n.bit_length()
	while(n):
		nReverse <<= 1
		nReverse |= (n & 1)
		s -= 1
		n >>= 1
	nReverse <<= s	
	print nReverse

n = 4
print n
reverse_number(n)

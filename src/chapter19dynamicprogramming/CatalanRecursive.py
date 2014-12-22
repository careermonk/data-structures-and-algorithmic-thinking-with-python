# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def CatalanRecursive(n):
	if n == 0:
		return 1
	else:
		count = 0
		for i in range(n):
			count += CatalanRecursive(i) * CatalanRecursive(n - 1 - i)
		return count	

print CatalanRecursive(4)

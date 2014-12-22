# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 


def Function(n):
	count = 0
	for i in range(n / 2, n):  # Outer loop execute n/2 times
		j = 1
		while j + n / 2 <= n:  # Middle loop executes logn times
			k = 1
			while k <= n:  # Inner loop execute logn times
				count = count + 1
				k = k * 2
			j = j * 2

	print (count)

Function(20)

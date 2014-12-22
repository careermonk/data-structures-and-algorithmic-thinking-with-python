# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 


def function(n):
	if (n < 2):  # Constant time
		return
	else:
		counter = 0  # Constant time
	for i in range(1, 8):  # This loop executes 8 times with n value half in every call
		function (n / 2)
	for i in range(1, n ** 3):  # This loop executes n^3 times with constant time loop
		counter = counter + 1

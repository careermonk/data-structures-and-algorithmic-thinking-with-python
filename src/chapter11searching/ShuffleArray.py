# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import random
def shuffleArray(A):
	n = len(A)
	i = n - 1
	while i > 0:
		j = int((random.random()) % (i + 1))
		tmp = A[j - 1];A[j - 1] = A[j];A[j] = tmp
		i -= 1

A = [1, 3, 5, 6, 2, 4, 6, 8]
shuffleArray(A)
print A

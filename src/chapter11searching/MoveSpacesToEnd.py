# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def moveSpacesToEnd(A):
	n = len(A) - 1
	datalist = list(A)
	count = i = 0
	for i in range(i, n):
		if(not datalist[i].isspace()):
			datalist[count] = datalist[i]
			count += 1
			
	while(count <= n):
		datalist[count] = ' '
		count += 1
	A = ''.join(datalist)
	return A
A = "move these spaces to beginning"
print A, "\n", moveSpacesToEnd(A)


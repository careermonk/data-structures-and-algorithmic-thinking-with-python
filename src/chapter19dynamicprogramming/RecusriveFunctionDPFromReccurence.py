# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def f(n) :
	sum = 0
	if(n == 0 or n == 1):
		return 2 
	# Recursive case
	for i in range(1, n):
		sum += 2 * f(i) * f(i - 1)
	return sum


print f(4)



def f2(n) :
	T = [0] * (n + 1)
	T[0] = T[1] = 2
	for i in range(2, n + 1):
		T[i] = 0
		for j in range(1, i):
			T[i] += 2 * T[j] * T[j - 1]

	return T[n]

print f2(4)

def f3(n):
	T = [0] * (n + 1)
	T[0] = T[1] = 2
	T[2] = 2 * T[0] * T[1]
	for i in range(3, n + 1):
		T[i] = T[i - 1] + 2 * T[i - 1] * T[i - 2]
	return T[n]


print f3(4)

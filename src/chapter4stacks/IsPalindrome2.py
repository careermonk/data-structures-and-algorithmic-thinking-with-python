# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def isPalindrome(A):
	i = 0
	j = len(A) - 1
	while (i < j and A[i] == A[j]):
		i += 1
		j -= 1
	if (i < j):
		print("Not a Palindrome")
		return 0
	else:
		print("Palindrome")
		return 1

isPalindrome(['m', 'a', 'd', 'a', 'm'])

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
	if n <= 0:
		return
	for i in range(1, 3):  # This loop executes 3 times with recursive value of n/3  value
 		Function(n / 3)
Function(20)

def Function2(n):
	if n <= 0:
		return
	for i in range(1, 3):  # This loop executes 3 times with recursive value of n/3  value
 		Function2(n - 1)
Function2(20)

def Function3(n):
	if n <= 0:
		return
	for i in range(1, 3):  # This loop executes 3 times with recursive value of n/3  value
 		Function3(0.8 * n)
Function3(20)


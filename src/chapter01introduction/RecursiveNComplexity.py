# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 


count = 0
def function(n):
	global count
	count = 1
	if n <= 0:
		return
	for i in range(1, n):
		count = count + 1
	n = n // 2;
	function(n)
	print count

function(200)

def Function2(n):
	if n <= 0:
		return
	print ("*")
	Function2(n / 2)
	Function2(n / 2)
	print ("*")

function(20)

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def FirstRepeatedChar (str):
	size = len(str)
	count = [0] * (256)
	for i in range(size):
		if(count[ord(str[i])] == 1):
			print  str[i]
			break
		else:    
			count[ord(str[i])] += 1
	if(i == size):
		print "No Repeated Characters"
	return 0

FirstRepeatedChar(['C', 'a', 'r', 'e', 'e', 'r', 'm', 'o', 'n', 'k'])

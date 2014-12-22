# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def RemoveChars(str, removeTheseChars):
	table = {}  # hash
	temp = []
	# set true for all characters to be removed
	for char in removeTheseChars.lower():
		table[char] = 1
	index = 0
	for char in str.lower():
		if char in table:
			continue
		else:
			temp.append(char)
			index += 1
	return "".join(temp)

print RemoveChars("careermonk", "e")


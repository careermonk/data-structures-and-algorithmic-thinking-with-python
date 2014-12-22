# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# If the str is editable
def ReversingString(str):
	s = list(str)
	end = len(str) - 1
	start = 0
	while (start < end):
		temp = s[start]
		s[start] = s[end]
		s[end] = temp
		start += 1
		end -= 1
		
	return "".join(s)

str = "CareerMonk Publications."
print ReversingString(str)

def reverse(str):
  r = ""
  for c in str:
    r = c + r
  return r
str = "CareerMonk Publications."
print reverse(str)

def ReversingString(str):
	s = list(str)
	end = len(str) - 1
	start = 0
	result = []
	while (start < end):
		s[start], s[end] = s[end], s[start]
		start += 1
		end -= 1

	return "".join(s)

str = "CareerMonk Publications."
print ReversingString(str)

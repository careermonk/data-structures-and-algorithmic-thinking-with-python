# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# @param s, a string
# @return a string
def reverseWordsInSentence(self, s):
	result = []
	inWord = False
	for i in range(0, len(s)):
	    if (s[i] == ' ' or s[i] == '\t') and inWord:
		inWord = False
		result.insert(0, s[start:i])
		result.insert(0, ' ')
	    elif not (s[i] == ' ' or s[i] == '\t' or inWord):
		inWord = True
		start = i
	if inWord:
	    result.insert(0, s[start:len(s)])
	    result.insert(0, ' ')
	if len(result) > 0:
	    result.pop(0)
	return ''.join(result)

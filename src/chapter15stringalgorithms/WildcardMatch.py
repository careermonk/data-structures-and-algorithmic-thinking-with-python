# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def wildcardMatch(inputString, pattern):
    if len(pattern) == 0: 
	    return len(inputString) == 0
    # inputString can be empty
    if pattern[0] == '?':
        return len(inputString) > 0 and wildcardMatch(inputString[1:], pattern[1:])
    elif pattern[0] == '*':
        # match nothing or
        # match one and continue, AB* = A*
        return wildcardMatch(inputString, pattern[1:]) or \
               (len(inputString) > 0 and wildcardMatch(inputString[1:], pattern))
    else: 
        return len(inputString) > 0 and inputString[0] == pattern[0] and wildcardMatch(inputString[1:], pattern[1:])
    
    return 0

print wildcardMatch("cc", "c")
print wildcardMatch("cc", "cc")
print wildcardMatch("ccc", "cc")
print wildcardMatch("cc", "*")
print wildcardMatch("cc", "a*")
print wildcardMatch("ab", "?*")
print wildcardMatch("cca", "c*a*b")

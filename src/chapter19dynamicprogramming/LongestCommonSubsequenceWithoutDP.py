# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def LCSLength(X, Y):
    if not X or not Y:
        return ""
    x, m, y, n = X[0], X[1:], Y[0], Y[1:]
    if x == y:
        return x + LCSLength(m, n)
    else:
        return max(LCSLength(X, n), LCSLength(m, Y), key=len)
	
print (LCSLength('thisisatest', 'testingLCS123testing'))	

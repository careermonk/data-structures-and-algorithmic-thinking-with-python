# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def removeAdjacentDuplicates(str):
    stkptr = -1
    i = 0
    size = len(str)
    while i < size:
        if (stkptr == -1 or str[stkptr] != str[i]):
            stkptr += 1
            str[stkptr] = str[i]
            i += 1
        else:
            while i < size and str[stkptr] == str[i]:
                i += 1
            stkptr -= 1
    stkptr += 1
    str = str[0:stkptr]
    print str
removeAdjacentDuplicates(['6', '2', '4', '1', '2', '1', '2', '2', '1'])

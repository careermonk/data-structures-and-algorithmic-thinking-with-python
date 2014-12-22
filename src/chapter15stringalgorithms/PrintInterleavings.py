# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def PrintInterleavings(str1, str2):
    perms = []
    if len(str1) + len(str2) == 1:
        return [str1 or str2]
    if str1:
        for item in PrintInterleavings(str1[1:], str2):
            perms.append(str1[0] + item)
    if str2:
        for item in PrintInterleavings(str1, str2[1:]):
            perms.append(str2[0] + item)
    return perms
    
print PrintInterleavings("AB", "CD")    

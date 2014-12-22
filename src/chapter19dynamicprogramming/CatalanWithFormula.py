# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

catalan = []
 
# 1st term is 1
catalan.append(1)
 
for i in range (1, 1001):
    x = catalan[i - 1] * (4 * i - 2) / (i + 1)
    catalan.append(x)
 
 
def CatalanNumber(n):
    return catalan[n]
    
print CatalanRecursive(4)    

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def CatalanNumber(n):
        catalan = [1, 1] + [0] * n
        for i in range(2, n + 1):
            for j in range(n):
                catalan[i] += catalan[j] * catalan[i - j - 1]
        return catalan[n]

print CatalanNumber(4)  

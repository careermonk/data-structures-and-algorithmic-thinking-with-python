# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def editDistance(A, B):
    m = len(A) + 1
    n = len(B) + 1

    table = {}
    for i in range(m): table[i, 0] = i
    for j in range(n): table[0, j] = j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if A[i - 1] == B[j - 1] else 1
            table[i, j] = min(table[i, j - 1] + 1, table[i - 1, j] + 1, table[i - 1, j - 1] + cost)

    return table[i, j]

print(editDistance("Helloworld", "HalloWorld"))

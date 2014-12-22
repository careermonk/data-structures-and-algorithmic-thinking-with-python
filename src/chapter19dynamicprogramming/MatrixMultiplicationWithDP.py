# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import sys, time
gk = lambda i, j:str(i) + ',' + str(j)
MAX = sys.maxint
def matrixMultiplicationWithDP(p):
    n = len(p) - 1
    m = {}
    for i in xrange(1, n + 1):
        for j in xrange (i, n + 1):
            m[gk(i, j)] = MAX
    return lookup_chain(m, p, 1, n)

def lookup_chain(m, p, i, j):
    if m[gk(i, j)] < MAX:
        return m[gk(i, j)]
    if i == j:
        m[gk(i, j)] = 0
    else:
        for k in xrange(i, j):
            q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k + 1, j) + p[i - 1] * p[k] * p[j]
            if q < m[gk(i, j)]:
                m[gk(i, j)] = q
    return m[gk(i, j)]

p = [30, 35, 15, 5, 10, 20, 25, 5, 16, 34, 28, 19, 66, 34, 78, 55, 23]
print matrixMultiplicationWithDP(p)


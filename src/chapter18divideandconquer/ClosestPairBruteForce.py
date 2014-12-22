# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

from math import sqrt, pow
 
def distance(a, b):
  return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
 
def bruteMin(points, current=float("inf")):
  if len(points) < 2: return current
  else:
    head = points[0]
    del points[0]
    newMin = min([distance(head, x) for x in points])
    newCurrent = min([newMin, current])
    return bruteMin(points, newCurrent)

A = [(12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print bruteMin(A)

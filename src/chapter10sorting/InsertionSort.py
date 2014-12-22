# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def Insertionsort(A):
  for i in range(1, len(A)):
    tmp = A[i]
    k = i
    while k > 0 and tmp < A[k - 1]:
        A[k] = A[k - 1]
        k -= 1
    A[k] = tmp    
      
A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
Insertionsort(A)
print(A) 

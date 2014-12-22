# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def SelectionSort(A):
  for i in range(len(A)):
    least = i
    for k in range(i + 1 , len(A)):
      if A[k] < A[least]:
        least = k
 
    swap(A, least, i)
 
 
def swap(A, x, y):
  temp = A[x]
  A[x] = A[y]
  A[y] = temp
	      
      
A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
SelectionSort(A)
print(A) 

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def heapSort(A):
  # convert A to heap
  length = len(A) - 1
  leastParent = length / 2
  for i in range (leastParent, -1, -1):
    percolateDown(A, i, length)

  # flatten heap into sorted array
  for i in range (length, 0, -1):
    if A[0] > A[i]:
      swap(A, 0, i)
      percolateDown(A, 0, i - 1)

 # Modfied percolateDown to skip the sorted elements
def percolateDown(A, first, last):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if (largest < last) and (A[largest] < A[largest + 1]):
      largest += 1
  
    # right child is larger than parent
    if A[largest] > A[first]:
      swap(A, largest, first)
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      return  # force exit
  
def swap(A, x, y):
  temp = A[x]
  A[x] = A[y]
  A[y] = temp

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(heapSort(A))
print A

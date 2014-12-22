# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def insertionSort(A):
  for i in range(1, len(A)):
    temp = A[i]
    k = i
    while k > 0 and temp < A[k - 1]:
        A[k] = A[k - 1]
        k -= 1
    A[k] = temp    
    
def BucketSort(A):
  code = Hashing(A)
  buckets = [list() for _ in range(code[1])]
  for i in A:
    x = ReHashing(i, code)
    buck = buckets[x]
    buck.append(i)
    
  for bucket in buckets:
    insertionSort(bucket)
 
  ndx = 0
  for b in range(len(buckets)):
    for v in buckets[b]:
      A[ndx] = v
      ndx += 1
      
  return A
 
import math
 
def Hashing(A):
  m = A[0]
  for i in range(1, len(A)):
    if (m < A[i]):
      m = A[i]
  result = [m, int(math.sqrt(len(A)))]
  return result
  
def ReHashing(i, code):
  return int(i / code[0] * (code[1] - 1))
  
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(BucketSort(A))

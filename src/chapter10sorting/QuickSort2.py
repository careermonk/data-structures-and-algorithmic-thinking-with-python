# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def quickSort(A,low,high):
   if low >= high:
    return
   pivot = A[low]
   i = low+1
   j = high
   while i <= j:
       while i <= j and A[i] <= pivot:
           i = i + 1
       while A[j] >= pivot and j >= i:
           j = j -1
       if j < i:
           break
       A[i], A[j] = A[j], A[i]

   A[low], A[j] = A[j], A[low]
   partitionPoint = j

   quickSort(A,low,partitionPoint-1)
   quickSort(A,partitionPoint+1,high)

A = [5, 1, 32, 54, 12, 6, 32, 2, 5, 19, 99, 9]
quickSort(A,0,len(A)-1)
print(A)

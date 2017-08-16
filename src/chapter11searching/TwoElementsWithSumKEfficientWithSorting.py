# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def pair_sum_k_sorting(A, K):
    left = 0
    right = len(A) - 1; 
    while(left < right):
         if(A[left] + A[right] == K):
              return 1
         elif(A[left] + A[right] < K):
              left += 1
         else:
              right -= 1
    return 0
    
A = [1, 4, 45, 6, 10, -8]
A.sort()
print pair_sum_k_sorting(A, 11)

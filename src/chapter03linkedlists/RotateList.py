# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def rotateList(A, K):
    n = K % len(A)
    word = A[::-1]
    return A[n:] + word[len(A) - n:]
A = [7, 3, 2, 3, 3, 6, 3]
print A, rotateList(A, 3)

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def oddeven(A):
    "Odd-Even sort implementation"
    sorted = False
    while(not sorted):
        sorted = True
        for i in range(1, len(A) - 1, 2):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                sorted = False
        for i in range(0, len(A) - 1, 2):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                sorted = False
        if not sorted:
            print A

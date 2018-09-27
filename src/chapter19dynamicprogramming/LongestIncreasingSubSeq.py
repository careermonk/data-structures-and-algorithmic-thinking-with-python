# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2018-09-27 07:15:46 
# Last modification		: 2008-10-31 
#               by		: Abhimanyu Aryan 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def LongestIncreasingSequence(arr): 
    n = len(arr)  
    LISTable = [1]*n  
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
    # Initialize maximum to 0 to get the maximum of all LIS
    maximum = 0
    # Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum , lis[i]) 
    return maximum 

print(LongestIncreasingSequence([10, 22, 9, 33, 21, 50, 41, 60]))

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def longestPalindromeSubstring(A):
    n = len(A)
    if n == 0: return ''
    L = {}
    for i in range(n): L[(i, i)] = True
    # k = j-i between 0 and n-1
    for k in range(n - 1):
        for i in range(n):
            j = i + k
            if j >= n: continue
            if i + 1 <= j - 1:
                L[(i, j)] = L[(i + 1, j - 1)] and A[i] == A[j]
            else:
                L[(i, j)] = A[i] == A[j]
    start, end = max([k for k in L if L[k]],
                      key=lambda x:x[1] - x[0])
    return A[start:end + 1]
    
print longestPalindromeSubstring('cabcbaabac')
print longestPalindromeSubstring('abbaaa')
print longestPalindromeSubstring('')    

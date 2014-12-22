# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def matrixFind(matrix, value):
    m = len(matrix)
    if m == 0:
        return 0

    n = len(matrix[0])
    if n == 0:
        return 0

    i = 0
    j = n - 1

    while i < m and j >= 0:
        if matrix[i][j] == value:
            return 1

        elif matrix[i][j] < value:
            i = i + 1

        else:
            j = j - 1

    return 0

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def LongestIncreasingSequence(numList):
    LISTable = [1]
    for i in range(1, len(numList))):
        LISTable.append(1)
        for j in range(i + 1, n):
            if numList[i] < numList[j] and LISTable[i] < LISTable[j] + 1:
                LISTable[i] = 1 + LISTable[j]
    print LISTable
    return max(LISTable)

print LongestIncreasingSequence([3, 2, 6, 4, 5, 1])

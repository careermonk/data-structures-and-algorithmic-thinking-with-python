# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def combinationByRecursion(elems, s, idx, li):
    for i in range(idx, len(elems)):
        s += elems[i]
        li.append(s)
        # print s, idx
        combinationByRecursion(elems, s, i + 1, li)
        s = s[0:-1]

def combinationByIteration(elems):
    level = ['']
    for i in range(len(elems)):
        nList = []
        for item in level:
            nList.append(item + elems[i])
        level += nList
    return level[1:]

res = []
combinationByRecursion('abc', '', 0, res)
print combinationByIteration('abc')
print combinationByIteration('abc')

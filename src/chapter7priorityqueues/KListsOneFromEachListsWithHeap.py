# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import heapq

def KListsOneElementFromEach(Lst):
    heap = []
    end = False
    for l in Lst :
        thisRange = max(l) - min(l)
        heap.append(min(l))
        heapq.heapify(heap)
            
    while not end:
        elem = heapq.heappop(heap)
        print elem
        for l in Lst :            
            if elem in l:
                # print l                
                l.remove(elem)
                # print l
                if len(l) == 0:
                    end = True
                    break
                heapq.heappush(heap, l[0])
    print heap
    
def minL(l):
    m = min(float(s) for s in l)
    return m

def maxL(l):
    m = max(float(s) for s in l)
    return m

Lst = [[4, 10, 15, 24, 26], [0, 19, 12, 20], [15, 18, 28, 30], ]
KListsOneElementFromEach(Lst)

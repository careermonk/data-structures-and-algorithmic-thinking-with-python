# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

from heapq import heappush, heappop, heapify
from collections import defaultdict
 
def HuffmanEncode(characterFrequency):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[freq, [sym, ""]] for sym, freq in characterFrequency.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 
inputText = "this is an example for huffman encoding"
characterFrequency = defaultdict(int)
for character in inputText:
    characterFrequency[character] += 1
huffCodes = HuffmanEncode(characterFrequency)
print "Symbol\tFrequency\tHuffman Code"
for p in huffCodes:
    print "%s\t\t\t%s\t\t\t%s" % (p[0], characterFrequency[p[0]], p[1])

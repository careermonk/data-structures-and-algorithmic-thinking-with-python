# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import sys
def BellmanFord(G, source):
    destination = {} 
    predecessor = {} 
    for node in G:
        destination[node] = sys.maxint  # We start admiting that the rest of nodes are very very far
        predecessor[node] = None
    destination[source] = 0  # For the source we know how to reach
    for i in range(len(G) - 1): 
        for u in G:
            for v in G[u]:  # For each neighbour of u
		# If the distance between the node and the neighbour is lower than the one I have now
		if destination[v] > destination[u] + G[u][v]:
			# Record this lower distance
			destination[v] = destination[u] + G[u][v]
			predecessor[v] = u		
 
    # Step 3: check for negative-weight cycles
    for u in G:
        for v in G[u]:
            assert destination[v] <= destination[u] + G[u][v]
 
    return destination, predecessor	
    
if __name__ == '__main__':
	G = {
		'A': {'B':-1, 'C':  4},
		'B': {'C':  3, 'D':  2, 'E':  2},
		'C': {},
		'D': {'B':  1, 'C':  5},
		'E': {'D':-3}
	}
	print BellmanFord(G, 'A')

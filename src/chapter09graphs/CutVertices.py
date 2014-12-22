# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import math
adjMatrix = [[0 for x in G.numVertices] for x in G.numVertices]
dfsnum = [0] * G.numVertices
num = 0
low = [0] * G.numVertices
def CutVertices(G, u) :
	low[u] = num
	dfsnum[u] = num
	num = num + 1
	for v in range(0, G.numVertices):
		if(G.adjMatrix[u][v] and dfsnum[v] == -1):
			CutVertices(v) 
			if(low[v] > dfsnum[u]):
				print "Cut Vetex:", u
			low[u] = min (low[u] , low[v]) 
		 
		else:  # (u,v) is a back edge
			low[u ] = min(low[u] , dfsnum[v])

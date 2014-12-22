# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def DetectCycle(G) :
	for i in range(0, G.numVertices):
		Visited[s] = 0
		Predecessor[i] = 0
	
	for i in range(0, G.numVertices):
		if(not Visited[i] and HasCycle(G, i)):
			return 1
	return False

def HasCycle(G, u) :
	Visited[u] = 1
	for i in range(0, G.numVertices):
		if(G.adjMatrix[s][i]) :
			if(Predecessor[i] != u and Visited[i]):
				return 1
			else:
				Predecessor[i] = u
				return  HasCycle(G, i)
	return 0


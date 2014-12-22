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
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None
        # InDegree Count
        self.inDegree = 0	
        # OutDegree Count
        self.outDegree = 0	

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()  
	
    def setInDegree(self, inDegree):
        self.inDegree = inDegree
    def getInDegree(self):
        return self.inDegree

    def getVertexID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertDictionary.values())

    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None

    def addEdge(self, frm, to, cost=1):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
	self.vertDictionary[to].inDegree += 1

    def getVertices(self):
        return self.vertDictionary

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous
	
    def getEdges(self):
        edges = []
	for v in G:
		for w in v.getConnections():
		    vid = v.getVertexID()
		    wid = w.getVertexID()
		    edges.append((vid, wid, v.getWeight(w)))
	return edges

def topologicalSort(G):
	"""Perform a topological sort of the nodes. If the graph has a cycle,
	throw a GraphTopologicalException with the list of successfully
	ordered nodes."""
	# topologically sorted list of the nodes (result)
	topologicalList = []
	# queue (fifo list) of the nodes with inDegree 0
	topologicalQueue = []
	# {node: inDegree} for the remaining nodes (those with inDegree>0)
	remainingInDegree = {}
	
	nodes = G.getVertices()
	for v in G:
		indegree = v.getInDegree()
		if indegree == 0:
			topologicalQueue.append(v)
		else:
			remainingInDegree[v] = indegree

	# remove nodes with inDegree 0 and decrease the inDegree of their sons
	while len(topologicalQueue):
	    # remove the first node with degree 0
	    node = topologicalQueue.pop(0)
	    topologicalList.append(node)
	    # decrease the inDegree of the sons
	    for son in node.getConnections():
		son.setInDegree(son.getInDegree() - 1)
		if son.getInDegree() == 0:
		    topologicalQueue.append(son)

	# if not all nodes were covered, the graph must have a cycle
	# raise a GraphTopographicalException
	if len(topologicalList) != len(nodes):
	    return False
	    
	# Printing the topological order    
	while len(topologicalList):
		 node = topologicalList.pop(0)
		 print node.getVertexID()
	return True

def isDirectedAcyclicGraph(G):
    """Return True if the graph G is a directed acyclic graph (DAG).
    Otherwise return False.  
    """
    if topologicalSort(G) :
        return True
    else:
        return False	
	
if __name__ == '__main__':
    G = Graph()
    G.addVertex('A')
    G.addVertex('B')
    G.addVertex('C')
    G.addVertex('D')
    G.addVertex('E')
    G.addVertex('F')
    G.addVertex('G')
    G.addVertex('H')
    G.addVertex('I')
    G.addEdge('A', 'B')   
    G.addEdge('A', 'C')   
    G.addEdge('A', 'G')  
    G.addEdge('A', 'E')  
    G.addEdge('B', 'C')       
    G.addEdge('C', 'G')   
    G.addEdge('D', 'E')  
    G.addEdge('D', 'F')  
    G.addEdge('F', 'H')       
    G.addEdge('E', 'H')    
    G.addEdge('H', 'I')      	    
    print isDirectedAcyclicGraph(G)

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
        self.distance = sys.maxint - 10
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()  

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

    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
        self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)

    def getVertices(self):
        return self.vertDictionary.keys()

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.getVertexID())
        shortest(v.previous, path)
    return

import heapq

def dijkstraModifiedForPrims(G, source):
    print '''Dijkstra Modified for Prim'''
    # Set the distance for the source node to zero 
    source.setDistance(0)

    # Put tuple pair into the priority queue
    unvisitedQueue = [(v.getDistance(), v) for v in G]
    heapq.heapify(unvisitedQueue)

    while len(unvisitedQueue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisitedQueue)
        current = uv[1]
        current.setVisited()
        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            newCost = current.getWeight(next)
            
            if newCost < next.getDistance():
                next.setDistance(current.getWeight(next))
                next.setPrevious(current)
                print 'Updated : current = %s next = %s newCost = %s' \
                        % (current.getVertexID(), next.getVertexID(), next.getDistance())
            else:
                print 'Not updated : current = %s next = %s newCost = %s' \
                        % (current.getVertexID(), next.getVertexID(), next.getDistance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisitedQueue):
            heapq.heappop(unvisitedQueue)
        # 2. Put all vertices not visited into the queue
        unvisitedQueue = [(v.getDistance(), v) for v in G if not v.visited]
	heapq.heapify(unvisitedQueue)
    
if __name__ == '__main__':

    G = Graph()
    G.addVertex('A')
    G.addVertex('B')
    G.addVertex('C')
    G.addVertex('D')
    G.addVertex('E')
    G.addEdge("A", "B", 7)
    G.addEdge("A", "D", 5)
    G.addEdge("B", "C", 8)
    G.addEdge("B", "D", 9)
    G.addEdge("B", "E", 7)
    G.addEdge("C", "E", 5)
    G.addEdge("D", "E", 15)
    G.addEdge("D", "F", 6)
    G.addEdge("E", "F", 8)
    G.addEdge("E", "G", 9)
    G.addEdge("F", "G", 11)
    
    print 'Graph data:'
    for v in G:
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            print '( %s , %s, %3d)' % (vid, wid, v.getWeight(w))
	    
    source = G.getVertex('A')
    dijkstraModifiedForPrims(G, source) 
    
    for v in G.vertDictionary.values():
	if v.previous:
		print v.getVertexID(), " to ", v.previous.getVertexID(), "-->", v.getDistance()
	else:
		print v.getVertexID(), " to None -->", v.getDistance()

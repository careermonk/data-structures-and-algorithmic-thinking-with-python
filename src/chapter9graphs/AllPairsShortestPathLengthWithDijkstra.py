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

def dijkstra(G, source):
    print '''Dijkstra's shortest path'''
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
            newDist = current.getDistance() + current.getWeight(next)
            
            if newDist < next.getDistance():
                next.setDistance(newDist)
                next.setPrevious(current)
                print 'Updated : current = %s next = %s newDist = %s' \
                        % (current.getVertexID(), next.getVertexID(), next.getDistance())
            else:
                print 'Not updated : current = %s next = %s newDist = %s' \
                        % (current.getVertexID(), next.getVertexID(), next.getDistance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisitedQueue):
            heapq.heappop(unvisitedQueue)
        # 2. Put all vertices not visited into the queue
        unvisitedQueue = [(v.getDistance(), v) for v in G if not v.visited]
	heapq.heapify(unvisitedQueue)

def allPairsShortestPathLength(G, cutoff=None):
    """ Return dictionary of shortest path lengths between all nodes in G."""
    paths = {}
    for n in G:
        paths[n] = dijkstra(G, n, cutoff=cutoff)
    return paths 	
	
if __name__ == '__main__':

    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addEdge('a', 'b', 4)  
    G.addEdge('a', 'c', 1)
    G.addEdge('c', 'b', 2)
    G.addEdge('b', 'e', 4)
    G.addEdge('c', 'd', 4)
    G.addEdge('d', 'e', 4)

    print 'Graph data:'
    for v in G:
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            print '( %s , %s, %3d)' % (vid, wid, v.getWeight(w))
	    
    source = G.getVertex('a')
    destination = G.getVertex('e')    
    dijkstra(G, source) 
    
    for v in G.vertDictionary.values():
	print source.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance()
	
    path = [destination.getVertexID()]
    shortest(destination, path)
    print 'The shortest path from a to e is: %s' % (path[::-1])
    print allPairsShortestPathLength(G)

# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Node of a Singly Linked List
class Node:
	# constructor
	def __init__(self, data=None, next=None):
		self.data = data
		self.last = None
		self.next = next
	# method for setting the data field of the node    
	def set_data(self, data):
		self.data = data
	# method for getting the data field of the node   
	def get_data(self):
		return self.data
	# method for setting the next field of the node
	def set_next(self, next):
		self.next = next
	# method for getting the next field of the node    
	def get_next(self):
		return self.next
	# method for setting the last field of the node
	def setLast(self, last):
		self.last = last
	# method for getting the last field of the node    
	def getLast(self):
		return self.last	
	# returns true if the node points to another node
	def has_next(self):
		return self.next != None


class Queue(object):
	def __init__(self, data=None):
		self.front = None
		self.rear = None
		self.size = 0

	def enQueue(self, data):
		self.lastNode = self.front
		self.front = Node(data, self.front)
		if self.lastNode:
			self.lastNode.setLast(self.front)
		if self.rear is None:
			self.rear = self.front
		self.size += 1

	def queueRear(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.rear.get_data()

	def queueFront(self):
		if self.front is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.front.get_data()

	def deQueue(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		result = self.rear.get_data()
		self.rear = self.rear.last
		self.size -= 1
		return result

	def size(self):
		return self.size
	
import sys
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False
        # Mark all nodes color with white        
        self.color = 'white'  	
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
	
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color	

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
	# For directed graph do not add this
        self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)

    def getVertices(self):
        return self.vertDictionary.keys()

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

def dfs(G, u, visited):
    visited[u] = True  # mark the visited node 
    print "traversal: " + u.getVertexID()
    for neighbourNodes in u.getConnections():  # take a neighbouring node 
        if neighbourNodes not in visited:  # condition to check whether the neighbour node is already visited
            dfs(G, neighbourNodes, visited)  # recursively traverse the neighbouring node 
 
def BFSTraversal(G, s):
	global maxPathLength
	pathLength = 0
	start = G.getVertex(s)
	start.setDistance(0)
	start.setPrevious(None)
	vertQueue = Queue()
	vertQueue.enQueue(start)
	vertQueue.enQueue(None)
	while (vertQueue.size > 0):
		currentVert = vertQueue.deQueue()
		if(currentVert == None):
			pathLength += 1
			if vertQueue.size > 0:
				vertQueue.enQueue(None)
			continue
		print currentVert.getVertexID()
		for nbr in currentVert.getConnections():
			if (nbr.getColor() == 'white'):
				nbr.setColor('gray')
				nbr.setDistance(currentVert.getDistance() + 1)
				nbr.setPrevious(currentVert)
				vertQueue.enQueue(nbr)
			currentVert.setColor('black')
	if pathLength > maxPathLength:
		maxPathLength = pathLength
		
maxPathLength = 0	
def LongestPathInDAG(G):

	for v in G:
		if (v.getColor() == 'white'):
			BFSTraversal(G, v.getVertexID())
	return maxPathLength

if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addEdge('a', 'b', 1)  
    G.addEdge('a', 'c', 1)
    G.addEdge('b', 'd', 1)
    G.addEdge('b', 'e', 1)
    G.addEdge('c', 'd', 1)
    G.addEdge('c', 'e', 1)
    G.addEdge('d', 'e', 1)
    G.addEdge('e', 'a', 1)
    print 'Graph data:'
    print G.getEdges()

    print LongestPathInDAG(G)

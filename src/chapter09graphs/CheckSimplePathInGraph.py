# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class Graph(object):
    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.graphDictionary = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.graphDictionary.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.generateEdges()

    def addVertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.graphDictionary, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.graphDictionary:
            self.graphDictionary[vertex] = []

    def addEdge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graphDictionary:
            self.graphDictionary[vertex1].append(vertex2)
        else:
            self.graphDictionary[vertex1] = [vertex2]

    def generateEdges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.graphDictionary:
            for neighbour in self.graphDictionary[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.graphDictionary:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generateEdges():
            res += str(edge) + " "
        return res
	
    def checkForPath(self, source, destination, path=[]):
	""" find a path from source to destination in graph """
	graph = self.graphDictionary
	path = path + [source]
	if source == destination:
	    return path
	if source not in graph:
	    return None
	for vertex in graph[source]:
	    if vertex not in path:
		extendedPath = self.checkForPath(vertex, destination, path)
		if extendedPath: 
		    return extendedPath
	return None

if __name__ == "__main__":

    g = { "a" : ["b", "c"],
          "b" : ["d", "e"],
          "c" : ["d", "e"],
          "d" : ["e"],
          "e" : ["a"],
          "f" : []
        }
    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())
    
    pathResult = graph.checkForPath("a", "e") 
    if(pathResult == None):
	    print "No path between source and destination"
    else:
	    print pathResult
	    
    pathResult = graph.checkForPath("a", "f") 
    if(pathResult == None):
	    print "No path between source and destination"
    else:
	    print pathResult

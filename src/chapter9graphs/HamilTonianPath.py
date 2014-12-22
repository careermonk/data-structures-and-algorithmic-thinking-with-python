# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class Vertex(object):
    def __init__(self, node, *nodeList):
        self.i = node
        self.nodeList = list(nodeList)
 
    def __hash__(self):
        return self.i
 
    def reaches(self, vertex):
        ''' Can receive an integer or a Vertex
        '''
        if isinstance(vertex, int):
            return vertex in self.nodeList
 
        return self.reaches(vertex.i)
 
    def __str__(self):
        return '< ' + str(self.i) + '>'
 
    def __repr__(self):
        return self.__str__()
 
 
class Graph(object):
    def __init__(self):
        self.vList = {}
 
    def add(self, node, *nodeList):
        vertex = Vertex(node, *nodeList)
        self.vList[node] = vertex
 
    def hamiltonian(self, current=None, pending=None, destiny=None):
        ''' Returns a list of nodes which represent
        a hamiltonian path, or None if not found
        ''' 
        if pending is None:
            pending = self.vList.values()
 
        result = None
 
        if current is None:
            for current in pending:
                result = self.hamiltonian(current, [x for x in pending if x is not current], current)
                if result is not None:
                    break
        else:
            if pending == []: 
                if current.reaches(destiny):
                    return [current]
                else:
                    return None
 
            for x in [self.vList[v] for v in current.nodeList]:
                if x in pending:
                    result = self.hamiltonian(x, [y for y in pending if y is not x], destiny)
                    if result is not None:
                        result = [current] + result
                        break    
 
        return result
 
if __name__ == '__main__':
    G = Graph() 
    G.add(1, 2, 8, 11)
    G.add(2, 1, 6, 9)
    G.add(3, 6, 7, 9, 10)
    G.add(4, 5, 7, 10)
    G.add(5, 4, 8, 11)
    G.add(6, 2, 3, 8)
    G.add(7, 3, 4, 8)
    G.add(8, 1, 6, 7, 5)
    G.add(9, 2, 3, 11)
    G.add(10, 3, 4, 11)
    G.add(11, 1, 9, 10, 5)
    print G.hamiltonian()

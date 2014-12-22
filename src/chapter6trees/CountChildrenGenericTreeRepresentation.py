# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Implement simple generic tree which allows us to add children and also prints the path from root to leaves (nodes without children) for every node.

import string
class GenericTree:
    """ Generic n-ary tree node object
        Children are additive; no provision for deleting them.
        The birth order of children is recorded: 0 for the first
        child added, 1 for the second, and so on.
            GenericTree(parent, value=None)    Constructor
            parent         			If this is the root node, None, otherwise the parent's GenericTree object.
            childList      			List of children, zero or more GenericTree objects.
            value          			Value passed to constructor; can be any type.
            birthOrder     			If this is the root node, 0, otherwise the index of this child in the parent's .childList
            nChildren()    			Returns the number of self's children.
            nthChild(n)    			Returns the nth child; raises IndexError if n is not a valid child number.
            fullPath():    			Returns path to self as a list of child numbers.
            nodeId():     			Returns path to self as a NodeId.
    """
    def __init__ (self, parent, value=None):
        self.parent = parent
        self.value = value
        self.childList = []
        if  parent is None:
            self.birthOrder = 0
        else:
            self.birthOrder = len(parent.childList)
            parent.childList.append (self)
    def nChildren (self):
        return len(self.childList)

    def nthChild (self, n):
        return self.childList[n]

    def fullPath (self):
        result = []
        parent = self.parent
        kid = self
        while  parent:
            result.insert (0, kid.birthOrder)
            parent, kid = parent.parent, parent
        return result

    def nodeId (self):
        fullPath = self.fullPath()
        return NodeId (fullPath)

    def siblingCount (self):
        if  parent is None:
            return 1
	else:
            self.parent.nChildren

class NodeId:
    def __init__ (self, path):
        self.path = path

    def __str__ (self):
        L = map (str, self.path)
        return string.join (L, "/")

    def find (self, node):
        return self.__reFind (node, 0)

    def __reFind (self, node, i):
        if  i >= len(self.path):
            return node.value  # We're there!
        else:
            childNo = self.path[i]
        try:
            child = node.nthChild (childNo)
        except IndexError:
            return None
        return self.__reFind (child, i + 1)

    def isOnPath (self, node):
        if  len(nodePath) > len(self.path):
            return 0  # Node is deeper than self.path

        for  i in range(len(nodePath)):
            if  nodePath[i] != self.path[i]:
                return 0  # Node is a different route than self.path
        return 1

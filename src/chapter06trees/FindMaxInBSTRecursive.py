# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class BSTNode(object):
    '''
    A binary search tree (BST) node
    '''

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
	
    # set data
    def set_data(self, data):
        self.data = data
    # get data   
    def get_data(self):
        return self.data	
    # get left child of a node
    def getLeft(self):
        return self.left
    # get right child of a node
    def getRight(self):
        return self.right
    # get left child of a node
    def setLeft(self, left):
        self.left = left
    # get right child of a node
    def setRight(self, right):
        self.right = right
	
    def search(self, data):
        if self.data == data:
            return self

        if self.left is not None and self.data > data:
            return self.left.search(data)
        elif self.right is not None:
            return self.right.search(data)

        return None
    
    def insert(self, data):
        self.insertNode(BSTNode(data))

    def insertNode(self, node):
        '''
        Inserts a data to the tree with self as root
        
        @param data The data to be inserted
        '''
        # Base case: empty root node
        if self.data is None:
            self.data = node.data
            return

        if node.data < self.data:
            if not self.left:
                self.left = node
                self.left.parent = self
            else:
                self.left.insertNode(node)
        elif node.data > self.data:
            if not self.right:
                self.right = node
                self.right.parent = self
            else:
                self.right.insertNode(node)
        else:
            pass  # Duplicate values are ignored

    def delete(self, data):
        # Base case: root node
        if self.data == data:
            self.deleteNode()
        elif data < self.data and self.left is not None:
            self.left.delete(data)
        elif self.right is not None:
            self.right.delete(data)

    def deleteNode(self):
        '''
        Removes the node from its tree, updating its children node pointers, if any.
        @param parent the node's parent
        '''
        if self.right and self.left:
            # Node has two children Replace data with successor s and delete s
            if self.right:
                s = self.successor()
                self.data = s.data
                s.deleteNode()
        elif self.right or self.left:
            # Node has single child. Replace it with only child
            child = self.right is not None and self.right or self.left

            self.data = child.data

            self.left = child.left
            self.right = child.right

            if self.left : self.left.parent = self
            if self.right : self.right.parent = self
        else:
            # None has no children, erase data and update parent
            self.data = None

            if self.parent:
                if self is self.parent.left:
                    self.parent.left = None
                else:
                    self.parent.right = None

    def successor(self):
        s = None

        if self.right:
            s = self.right
            while s.left:
                s = s.left

        return s

    def predecessor(self):
        s = None

        if self.left:
            s = self.left
            while s.right:
                s = s.right

        return s

    def rotateRight(self):
        '''
              Q            P
             / \          / \
            P   C   ==>  A   Q
           / \              / \
          A   B            B   C
        '''
        # If you do not understand at first, note that instead of
        # moving Q to C's position, I move P instead. So think on
        # terms of "P will be future Q"
        Q, P = self, self.left
 
        if not P: return
      
        Q.left = P.left
        P.left = P.right
        P.right = Q.right
        Q.right = P
        
        if P.right: P.right.parent = P
        if Q.left: Q.left.parent = Q

        P.data, Q.data = Q.data, P.data

    def rotateLeft(self):
        '''
              Q             P
             / \           / \
            C   P   ==>   Q   B
               / \       / \
              A   B     C   A
        '''
        # If you do not understand at first, note that instead of
        # moving Q to C's position, I move P instead. So think on
        # terms of "P will be future Q"
        Q, P = self, self.right
 
        if not P: return
      
        Q.right = P.right
        P.right = P.left
        P.left = Q.left
        Q.left = P
        
        if P.left: P.left.parent = P
        if Q.right: Q.right.parent = Q

        P.data, Q.data = Q.data, P.data

    def __str__(self):
        return "(%s, l: %s, r: %s)" % (self.data, self.left is not None and self.left.data or 'N', self.right is not None and self.right.data or 'N')

def inorderRecursive(root):
	if not root:
		return
	inorderRecursive(root.left)
	print root.data
	inorderRecursive(root.getRight())


# Search the key from node, iteratively
def findMaxIterative(root):
	currentNode = root
	if currentNode == None:  
		return None
	while currentNode.getRight() != None:
		currentNode = currentNode.getRight()
	return currentNode.get_data()

# Search the key from node, iteratively
def findMaxRecursive(root):
	currentNode = root
	if currentNode.getRight() == None:
		return currentNode.get_data()
	else:
		return findMaxRecursive(currentNode.getRight())

	
root = BSTNode(11)
root.insert(1)
root.insert(10)
root.insert(1100)
root.insert(5)
# inorderRecursive(root)
root.insert(2)
# inorderRecursive(root)
print findMaxRecursive(root)

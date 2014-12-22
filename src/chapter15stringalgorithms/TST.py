# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class TSTNode:
    def __init__ (self, x):
        self.data = x
        self.left = None
        self.eq = None
        self.right = None

# Search
def _search (node, x):
    while node:
        if node.data == x: return node
        if x < node.data:
            node = node.left
        else:
            node = node.right
    return None

# Insert
def _insert (node, x):
    if node is None: return x
    elif x.data == node.data: return node
    elif x.data < node.data:
        node.left = _insert (node.left, x)
    else:
        node.right = _insert (node.right, x)
    return node

# I Find the minimum value
def _searchMin (node):
    if node.left is None: return node.data
    return _searchMin (node.left)

# I want to delete the minimum value
def _deleteMin (node):
    if node.left is None: return node.right
    node.left = _deleteMin (node.left)
    return node

# Delete
def _delete (node, x):
    if node:
        if x == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.data = _searchMin (node.right)
                node.right = _deleteMin (node.right)
        elif x < node.data:
            node.left = _delete (node.left, x)
        else:
            node.right = _delete (node.right, x)
    return node

# Traverse
def _traverse (node, leaf):
    if node:
        for x in _traverse (node.left, leaf):
            yield x
        if node.data == leaf:
            yield []
        else:
            for x in _traverse (node.eq, leaf):
                yield [node.data] + x
        for x in _traverse (node.right, leaf):
            yield x


##### Ternary Search Tree #####

class TST:
    def __init__ (self, x=None):
        self.root = TSTNode (None)  # header
        self.leaf = x

    # Search
    def search (self, seq):
        node = self.root
        for x in seq:
            node = _search (node.eq, x)
            if not node: return False
        # Check leaf
        return _search (node.eq, self.leaf) is not None

    # Insert
    def insert (self, seq):
        node = self.root
        for x in seq:
            child = _search (node.eq, x)
            if not child:
                child = TSTNode (x)
                node.eq = _insert (node.eq, child)
            node = child
        # Check leaf
        if not _search (node.eq, self.leaf):
            node.eq = _insert (node.eq, TSTNode (self.leaf))

    # Delete
    def delete (self, seq):
        node = self.root
        for x in seq:
            node = _search (node.eq, x)
            if not node: return False
        # Delete leaf
        if _search (node.eq, self.leaf):
            node.eq = _delete (node.eq, self.leaf)
            return True
        return False

    # Patrol
    def traverse (self):
        for x in _traverse (self.root.eq, self.leaf):
            yield x

    # I ask the data with a common prefix
    def commonPrefix (self, seq):
        node = self.root
        buff = []
        for x in seq:
            buff.append (x)
            node = _search (node.eq, x)
            if not node: return
        for x in _traverse (node.eq, self.leaf):
            yield buff + x

# Simple test
if __name__ == '__main__':
    # Suffix trie
    def makeTST (seq):
        a = TST ()
        for x in xrange (len (seq)):
            a.insert (seq [x:])
        return a

    s = makeTST ('abcabbca')
    for x in s.traverse ():
        print x
    for x in ['a', 'bc']:
        print x
        for y in s.commonPrefix (x):
            print y
    print s.delete ('a')
    print s.delete ('ca')
    print s.delete ('bca')
    for x in s.traverse ():
        print x
    s = makeTST ([0, 1, 2, 0, 1, 1, 2, 0])
    for x in s.traverse ():
        print x

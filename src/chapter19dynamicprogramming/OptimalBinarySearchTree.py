# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class OptimalBinarySearchTree(BSTNode):  # For BSTNode, refer Trees chapter
    def __init__(self):
        super(OptimalBinarySearchTree, self).__init__()
        self.num_keys = 0
        self.keys = []
        self.probabilities = []
        self.dummyProbabilities = [1]

    def optimalBST(self):
        n = len(self.keys) + 1
        root_matrix = [[0 for i in xrange(n)] for j in xrange(n)]
        probabilitiesSumMatrix = [[0 for i in xrange(n)] for j in xrange(n)]
        expectedCostMatrix = [[99999 for i in xrange(n)] for j in xrange(n)]
        for i in xrange(1, n):
            probabilitiesSumMatrix[i][i - 1] = self.dummyProbabilities[i - 1]
            expectedCostMatrix[i][i - 1] = self.dummyProbabilities[i - 1]

        for l in xrange(1, n):
            for i in xrange(1, n - l):
                j = i + l - 1
                expectedCostMatrix[i][j] = 99999
                probabilitiesSumMatrix[i][j] = probabilitiesSumMatrix[i][j - 1] + self.probabilities[j] + self.dummyProbabilities[j]
                for r in xrange(i, j + 1):
                    t = expectedCostMatrix[i][r - 1] + expectedCostMatrix[r + 1][j] + probabilitiesSumMatrix[i][j]
                    if t < expectedCostMatrix[i][j]:
                        expectedCostMatrix[i][j] = t
                        root_matrix[i][j] = r
        return root_matrix

    def constructOptimalBST(self):
        root = self.optimalBST()
        n = self.num_keys
        r = root[1][n]
        value = self.keys[r]
        self.insert(value)
        self.constructOptimalSubtree(1, r - 1, r, "left", root)
        self.constructOptimalSubtree(r + 1, n, r, "right", root)

    def constructOptimalSubtree(self, i, j, r, direction, root):
        if i <= j:
            t = root[i][j]
            value = self.keys[t]
            self.insert(value)
            self.constructOptimalSubtree(i, t - 1, t, "left", root)
            self.constructOptimalSubtree(t + 1, j, t, "right", root)

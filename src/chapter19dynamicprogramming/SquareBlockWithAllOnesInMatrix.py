# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def squareBlockWithAllOnesInMatrix(matrix, ZERO=0):
    nrows, ncols = len(matrix), (len(matrix[0]) if matrix else 0)
    if not (nrows and ncols): return 0  # empty matrix or rows
    Table = [[0] * ncols for _ in xrange(nrows)]
    for i in reversed(xrange(nrows)):  # for each row
        assert len(matrix[i]) == ncols  # matrix must be rectangular
        for j in reversed(xrange(ncols)):  # for each element in the row
            if matrix[i][j] != ZERO:
                Table[i][j] = (1 + min(
                    Table[i][j + 1],  # east
                    Table[i + 1][j],  # south
                    Table[i + 1][j + 1]  # south-east
                    )) if i < (nrows - 1) and j < (ncols - 1) else 1  # edges
    return max(c for rows in Table for c in rows)
	    
matrix = [[0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
print squareBlockWithAllOnesInMatrix(matrix)

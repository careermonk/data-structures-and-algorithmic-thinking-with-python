# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def spiral_iterative(n):
    dx, dy = 1, 0  # Starting increments
    x, y = 0, 0  # Starting location
    matrix = [[None] * n for j in range(n)]
    for i in xrange(n ** 2):
        matrix[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return matrix
 
def print_spiral(matrix):
    n = range(len(matrix))
    for y in n:
        for x in n:
            print "%2i" % matrix[x][y],
        print
 
print_spiral(spiral_iterative(5))

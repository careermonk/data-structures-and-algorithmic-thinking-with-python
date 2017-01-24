# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail                   : info@careermonk.com 
# Creation Date            : 2014-01-10 06:15:46 
# Last modification        : 2008-10-31 
#               by        : Narasimha Karumanchi 
# Book Title            : Data Structures And Algorithmic Thinking With Python
# Warranty                 : This software is provided "as is" without any 
#                    warranty; without even the implied warranty of 
#                     merchantability or fitness for a particular purpose. 
 
#Printing the matrix
def print_matrix(matrix):
    for row in matrix:
        print row
    print
 
#rotate the matrix by 90 degrees (clockwise) in place
def rotate_90_degrees(matrix):
    layers = len(matrix) / 2
    length = len(matrix) - 1
 
    for layer in range(layers): #for each layer
        for i in range(layer, length - layer): # loop through the elements we need to change at each layer
            temp = matrix[layer][i] #save the top element, it takes just one variable as extra memory
            #Left -> Top
            matrix[layer][i] = matrix[length - i][layer]
            #Bottom -> left
            matrix[length - i][layer] = matrix[length - layer][length - i]
            #Right -> bottom
            matrix[length - layer][length - i] = matrix[i][length - layer]
            #Top -> Right
            matrix[i][length - layer] = temp
 
matrix =[ 
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ]  
        ]
print "Input matrix:\n"
print_matrix(matrix)
rotate_90_degrees(matrix)
print "Rotated matrix by 90 degrees:\n"
print_matrix(matrix)

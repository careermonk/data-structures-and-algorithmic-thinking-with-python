# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import sys
def preComputeMatrix(A, n):
	global Aux
	for i in range (0, n):
		for j in range (0, n):
			if(i == 0 and j == 0):
				Aux[i][j] = A[i][j]
			elif(i == 0):
				Aux[i][j] += Aux[i][j - 1] + A[i][j]
			elif(j == 0):
				Aux[i][j] += Aux[i - 1][j] + A[i][j]
			else:
				Aux[i][j] += Aux[i - 1][j] + Aux[i][j - 1] - Aux[i - 1][j - 1] + A[i][j]

def computeSum(A, i1, i2, j1, j2):
	if(i1 == 0 and j1 == 0):
		return Aux[i2][j2]
	elif(i1 == 0):
		return Aux[i2][j2] - Aux[i2][j1 - 1]
	elif(j1 == 0):
		return Aux[i2][j2] - Aux[i1 - 1][j2]
	else:
		return Aux[i2][j2] - Aux[i2][j1 - 1] - Aux[i1 - 1][j2] + Aux[i1 - 1][j1 - 1]

def getSubmatSum(r1, c1, r2, c2) :
	if (r1 == 0 and c1 == 0):
		return Aux[r2][c2]
	if (r1 == 0):
		return Aux[r2][c2] - Aux[r2][c1 - 1]
	if (c1 == 0):
		return Aux[r2][c2] - Aux[r1 - 1][c2]
	return Aux[r2][c2] - Aux[r1 - 1][c2] - Aux[r2][c1 - 1] + Aux[r1 - 1][c1 - 1]
 

def getMaxMatrix(A, n):
	globalmax = 0
	for i in range (0, n):
		for j in range (i, n):
			localmax = 0
			for k in range (0, n):
				localmax = max(localmax + getSubmatSum(i, k, j, k), 0)
				globalmax = max(localmax, globalmax)
	return globalmax

 
A = [[-1, -2, 13, -4], [-5, -6, -7, -8 ], [-9, 10, -11, -12] , [-13, -14, -15, -16]]
n = 4
Aux = [[0 for x in range(n)] for x in range(n)]
preComputeMatrix(A, n)
print getMaxMatrix(A, n)

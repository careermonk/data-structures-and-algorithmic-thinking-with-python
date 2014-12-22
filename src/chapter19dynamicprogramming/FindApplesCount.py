# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def FindApplesCount(Apples, n, m):
	S = [[0 for x in range(m)] for x in range(n)]
	S[0][0] = Apples[0][0]
	for i in range(1, n):
		S[i][0] = Apples[i][0] + S[i - 1][0]
		
	for j in range(1, m):
		S[0][j] = Apples[0][j] + S[0][j - 1]

	for i in range(1, n):
		for j in range(1, m):
			r1 = S[i][j - 1]
			r2 = S[i - 1][j]
			if (r1 > r2):
				S[i][j] = Apples[i][j] + r1
			else:
				S[i][j] = Apples[i][j] + r2

	return S[n - 1][m - 1]

Apples = [ [5, 24], [15, 25], [27, 40], [50, 60] ]
print FindApplesCount(Apples, 4, 2)

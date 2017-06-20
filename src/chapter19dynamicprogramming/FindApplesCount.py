# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def find_maximum_apples_count(Apples, n, m):
	S =[[0 for x in range(m)] for x in range(n)]

	# Initialize position S[0][0]. 
	# We cannot collect any apples otherthan Apples[0][0]
	S[0][0] = Apples[0][0]

	# Initialize the first row
	for j in range(1, m):
		S[0][j] = Apples[0][j] + S[0][j-1]	

	# Initialize the first column
	for i in range(1, n):
		S[i][0] = Apples[i][0] + S[i-1][0]

	for i in range(1, n):
		for j in range(1, m):
			previous_column = S[i][j-1]
			previous_row = S[i-1][j]

			if (previous_column > previous_row):
				S[i][j] =  Apples[i][j] + previous_column
			else:
				S[i][j] = Apples[i][j ]+ previous_row
	
	return S[n-1][m-1]

Apples = [ [1, 2, 4, 7], [2, 1, 6, 1], [12, 5, 9, 19], [4, 29, 50, 60] ]
print find_maximum_apples_count(Apples, len(Apples), len(Apples[0]))

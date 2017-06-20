def find_maximum_apples_count_3ways_of_reaching(Apples, n, m):
	S =[[0 for x in range(m)] for x in range(n)]

	# Initialize position S[0][0]. 
	# We cannot collect any apples other than Apples[0][0]
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
			previous_diagonal = S[i-1][j-1]
			
			if (previous_column >= previous_row) and (previous_column >= previous_diagonal):
			   largest = previous_column
			elif (previous_row >= previous_column) and (previous_row >= previous_diagonal):
			   largest = previous_row
			else:
			   largest = previous_diagonal

			S[i][j] =  Apples[i][j] + largest
	
	return S[n-1][m-1]

Apples = [ [1, 2, 4, 7], [2, 1, 6, 1], [12, 5, 9, 19], [4, 29, 50, 60] ]
print find_maximum_apples_count_3ways_of_reaching(Apples, len(Apples), len(Apples[0]))

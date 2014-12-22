# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def Knapsack(knapsackSize, itemsValue, itemsWeight):
	numItems = len(itemsValue)
	M = [[0 for x in range(knapsackSize + 1)] for x in range(len(itemsValue))]
	for i in range(1, numItems):
		for j in range(knapsackSize + 1):
			value = itemsValue[i]
			weight = itemsWeight[i]
			if weight > j:
				M[i][j] = M[i - 1][j]
			else:
				M[i][j] = max(M[i - 1][j], M[i - 1][j - weight] + value)
 
	return M[numItems - 1][knapsackSize]
	
print Knapsack(50, [60, 100, 120], [10, 20, 30])	

def findMin(A, i, j):
	min = A[i]
	while i <= j:
		if min > A[i]:
			min = A[i]
		i = i + 1
	return min

def largestHistrogram(A):
	maxArea = 0
	print A
	for i in range(len(A)):
		for j in range(i, len(A)):
			minimum_height = A[i]
			minimum_height = findMin(A, i, j)
			maxArea = max(maxArea, (j-i+1) * minimum_height)
	return maxArea


A = [6, 2, 5, 4, 5, 1, 6] 
print "largestRectangleArea: ", largestHistrogram(A)

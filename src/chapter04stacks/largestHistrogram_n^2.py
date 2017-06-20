
def largestHistrogram(A):
	maxArea = 0
	for i in range(len(A)):
		minimum_height = A[i]
		for j in range(i, len(A)):
			minimum_height = min(minimum_height, A[j])
			maxArea = max(maxArea, (j-i+1) * minimum_height)
	return maxArea


A = [6, 2, 5, 4, 5, 1, 6] 
print "largestRectangleArea: ", largestHistrogram(A)

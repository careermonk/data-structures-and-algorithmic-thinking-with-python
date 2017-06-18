def find_peak(A):
	max_peak_value = max_peak_index = -1
	peak = A[0]
	index = 0
	for i in range(1, len(A)-1):
		prev = A[i-1]
		curr = A[i]
		next = A[i+1]
		if curr > prev and curr > next:
			index = i
			peak = curr
		if peak > max_peak_value:
			max_peak_value, max_peak_index = peak, index

	if A[len(A)-1] > peak:
		return A[len(A)-1], len(A)-1

	return max_peak_value, max_peak_index

A = [35, 5, 20, 2, 90, 25, 80, 25, 115, 40]
print A, "\n", find_peak(A)

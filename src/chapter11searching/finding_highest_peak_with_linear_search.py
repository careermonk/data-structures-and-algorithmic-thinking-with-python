def find_peak(A):
	peak = A[0]
	for i in range(1, len(A)-2):
		prev = A[i-1]
		curr = A[i]
		next = A[i+1]
		if curr > prev and curr > next:
			index = i
			peak = curr

        if len(A)-1 > peak:
            return A[len(A)-1]
 
        return A[index]

A = [35, 5, 20, 2, 40, 25, 80, 25, 15, 40]
print A, "\n", find_peak(A)

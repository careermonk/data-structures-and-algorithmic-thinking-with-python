def find_peak(A):
    if not A:
        return -1

    left, right = 0, len(A) - 1
    while left + 1 < right:
        mid = left + (right - left) / 2
        if A[mid] < A[mid - 1]:
            right = mid
        elif A[mid] < A[mid + 1]:
            left = mid
        else:
            return mid
    mid = left if A[left] > A[right] else right
    return mid

A = [35, 5, 20, 2, 40, 25, 80, 25, 15, 40]
peak = find_peak(A)
print A, "\n", A[peak]

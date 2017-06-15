def find_peak(A):
    if not A:
        return -1

    l, r = 0, len(A) - 1
    while l + 1 < r:
        mid = l + (r - l) / 2
        if A[mid] < A[mid - 1]:
            r = mid
        elif A[mid] < A[mid + 1]:
            l = mid
        else:
            return mid
    mid = l if A[l] > A[r] else r
    return mid

A = [35, 5, 20, 2, 40, 25, 80, 25, 15, 40]
p = find_peak(A)
print A, "\n", A[p]

def LCS(X, Y):
    if not X or not Y:
        return ""
    x, m, y, n = X[0], X[1:], Y[0], Y[1:]
    if x == y:
        return x+LCS(m, n)
    else:
        # Use key=len to select the maximum string in a list efficiently
        return max(LCS (X, n), LCS(m, Y), key=len)

print "Longest common subsequence: ", LCS('ABCBDAB', 'BDCABA')

def LCS_length(X, Y):
    if not X or not Y:
        return 0
    x, m, y, n = X[0], X[1:], Y[0], Y[1:]
    if x == y:
        return 1+LCS_length(m, n)
    else:
        # Use key=len to select the maximum string in a list efficiently
        return max(LCS_length(X, n), LCS_length(m, Y))

print "Longest common subsequence length: ", LCS_length('ABCBDAB', 'BDCABA')

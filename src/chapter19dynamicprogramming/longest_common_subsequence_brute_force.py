def LCS_length(X, Y, i, j):
    if i == -1 or j == -1:
        return 0
    if X[i] == Y[j]:
        return 1 + LCS_length(X, Y, i-1, j-1)
    return max(LCS_length(X, Y, i-1, j), LCS_length(X, Y, i, j-1))

X = "ABCBDAB"
Y = "BDCABA"
print "Longest common subsequence: ", LCS_length(X, Y, len(X)-1, len(Y)-1)

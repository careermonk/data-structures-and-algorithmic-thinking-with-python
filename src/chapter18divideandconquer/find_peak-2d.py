import random
import pprint

def peak_find_2d(matrix):
    j = len(matrix[0]) // 2

    # maxvalue is the global maximum in column j
    # rowmax is the row index of the maxvalue
    maxvalue, rowmax = -1, -1
    for row in range(len(matrix)):
        if maxvalue <= matrix[row][j]:
            maxvalue = matrix[row][j]
            rowmax = row

    left, right = 0, 0
    if j > 0:
        left = matrix[rowmax][j - 1]
    if j < len(matrix[0]) - 1:
        right = matrix[rowmax][j + 1]
    if left <= maxvalue >= right:
        return (rowmax, j, maxvalue)
    if left > maxvalue:
        half = []
        for row in matrix:
            half.append(row[:j + 1])
        return peak_find_2d(half)
    if right > maxvalue:
        half = []
        for row in matrix:
            half.append(row[j:])
        return peak_find_2d(half)

def generate_2d_array(n=7, m=7, lower=0, upper=9):
    return [[random.randint(lower, upper) for _ in range(m)] for _ in range(n)]

if __name__ == '__main__':
    matrix = generate_2d_array(upper=9)
    pprint.pprint(matrix)
    x = peak_find_2d(matrix)
    pprint.pprint(x)

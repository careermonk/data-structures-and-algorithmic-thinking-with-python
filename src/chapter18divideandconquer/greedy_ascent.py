import random
import pprint
import operator
def greedy_ascent(matrix):
    j = len(matrix[0]) // 2
    i = len(matrix) // 2

    while True:
      left, right, up, bottom = 0, 0, 0, 0
      if j > 0:
          left = matrix[i][j - 1]
      if j < len(matrix[0]) - 1:
          right = matrix[i][j + 1]
      if i > 0:
          up = matrix[i-1][j]
      if i < len(matrix) - 1:
          bottom = matrix[i+1][j]
      if (left <= matrix[i][j] >= right) and (up <= matrix[i][j] >= bottom):
          return (i, j, matrix[i][j])
      my_list = [left, up, right, bottom]
      max_neighbor_index, max_neighbor_value = max(enumerate(my_list), key=operator.itemgetter(1))
      if max_neighbor_index == 0:
          j = j - 1
      elif max_neighbor_index == 1:
          i = i - 1
      elif max_neighbor_index == 2:
          j = j + 1
      else:
          i = i + 1


def generate_2d_array(n=7, m=7, lower=0, upper=9):
    return [[random.randint(lower, upper) for _ in range(m)] for _ in range(n)]

if __name__ == '__main__':
    matrix = generate_2d_array(upper=9)
    pprint.pprint(matrix)
    x = greedy_ascent(matrix)
    pprint.pprint(x)

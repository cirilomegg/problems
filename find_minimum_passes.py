# Find minimum passes required to convert all negative values in the matrix
# Given a M x N matrix of integers whose each cell can contain a negative, zero or positive value,
# determine the minimum number of passes required to convert all negative values in the matrix to positive.

# Only a non-zero positive value at cell(i, j) can convert negative values present at its adjacent cells(i-1, j),
# (i+1, j), (i, j-1), and (i, j+1) i.e. up, down, left and right.

def get_passes(matrix):
    pass


m = [
    [-1, -9, 0, -1, 0],
    [-8, -3, -2, 9, -7],
    [2, 0, 0, -6, 0],
    [0, -7, -3, 5, -4]
]
print(get_passes(m))

"""flip takes a matrix M with m rows and n columns and must hand back a new matrix with n rows and m columns,
in which row j holds column j of M: flip([[1, 2, 3], [4, 5, 6]]) must return [[1, 4], [2, 5], [3, 6]].
Its body is a single return, followed by one of the expressions below.
One of A to G is right: pick it, and say what each of the others returns instead.

Uncomment one candidate at a time to run it.
"""

def flip(M):
    # A
    # return [[M[i][j] for j in range(len(M[0]))] for i in range(len(M))]
    # B
    # return [M[i][j] for j in range(len(M[0])) for i in range(len(M))]
    # C
    # return [[M[i][j] for i in range(len(M))] for j in range(len(M))]
    # D
    # return [[M[j][i] for i in range(len(M))] for j in range(len(M[0]))]
    # E
    # return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
    # F
    # return [[row[j] for j in range(len(M[0]))] for row in M[::-1]]
    # G
    # return [[row[::-1][j] for row in M] for j in range(len(M[0]))]
    return None  # a placeholder: an uncommented return above ends the function before this line

print(flip([[1, 2, 3], [4, 5, 6]]))

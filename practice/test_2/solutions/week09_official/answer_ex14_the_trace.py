"""Mathematics calls the sum of the main diagonal the trace of a square matrix.
Write the program that computes and prints it, so that it stays right for any square matrix:
add a fourth row and column, and it should not change by one character.
One loop is enough (tip: the two indexes are the same).

The output to produce:
>>> 14
"""

m = [[7, 2, 9], [4, 1, 5], [3, 8, 6]]
trace = 0
for i in range(len(m)):
    trace = trace + m[i][i]
print(trace)  # 14

# The diagonal is m[i][i] — the two indexes are the same — and
# range(len(m)) takes the size from the matrix itself, so a fourth
# row and column change nothing.

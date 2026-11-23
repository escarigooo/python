"""The program ends with print(M), which must show [[0, 0, 0], [0, 0, 9]] —
a 2-by-3 grid of zeros with the second row’s third element set to 9.

Choose the fragment that builds it. One of A to D is right: pick it,
and say what each of the others does instead."""

# A - the right one
M = [[0, 0, 0], [0, 0, 0]]
M[1][2] = 9

# B - one list named twice: both rows show the 9 -> [[0, 0, 9], [0, 0, 9]]
# row = [0, 0, 0]
# M = [row, row]
# M[1][2] = 9

# C - counts from 1 -> IndexError: list index out of range
# M = [[0, 0, 0], [0, 0, 0]]
# M[2][3] = 9

# D - == compares instead of assigning: the grid prints unchanged -> [[0, 0, 0], [0, 0, 0]]
# M = [[0, 0, 0], [0, 0, 0]]
# M[1][2] == 9

print(M)  # [[0, 0, 0], [0, 0, 9]]

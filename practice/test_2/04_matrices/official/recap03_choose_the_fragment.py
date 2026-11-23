"""The program ends with print(M), which must show [[0, 0, 0], [0, 0, 9]] —
a 2-by-3 grid of zeros with the second row’s third element set to 9.

Choose the fragment that builds it. One of A to D is right:
pick it, and say what each of the others does instead."""

# Uncomment one candidate at a time, run, and compare with the target.

# A
# M = [[0, 0, 0], [0, 0, 0]]
# M[1][2] = 9

# B
# row = [0, 0, 0]
# M = [row, row]
# M[1][2] = 9

# C
# M = [[0, 0, 0], [0, 0, 0]]
# M[2][3] = 9

# D
# M = [[0, 0, 0], [0, 0, 0]]
# M[1][2] == 9

print(M)

# >>> [[0, 0, 0], [0, 0, 9]]

"""Read the program below and write the exact lines it prints, in order, and say how many there are.
On paper, before any run. Then run it and compare.
"""

m = [[7, 2, 9], [4, 1, 5]]
print(m[1][0])
print(m[0][2])
print(len(m), len(m[0]))

# The program prints three lines:
# 4
# 9
# 2 3

# m[1] is the second row [4, 1, 5], and its item 0 is 4;
# m[0][2] is 9.
# len(m) counts the rows, len(m[0]) the values in a row.

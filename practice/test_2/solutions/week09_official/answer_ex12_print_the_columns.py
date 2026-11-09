"""Write a program that prints the columns of the matrix — the first column on the first line,
then the second, then the third, exactly as the output below shows.
Use this lecture’s m[i][j], and think with care about which counter the outer loop must run.

The output to produce:
>>> 7 4 3
>>> 2 1 8
>>> 9 5 6
"""

m = [[7, 2, 9], [4, 1, 5], [3, 8, 6]]
for j in range(3):
    for i in range(3):
        print(m[i][j], end=" ")
    print()

# The program prints:
# 7 4 3
# 2 1 8
# 9 5 6

# The column index j moves slowly, so it drives the outer loop;
# the read is still m[i][j].

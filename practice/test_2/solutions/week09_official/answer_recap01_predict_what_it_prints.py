"""Read the program below and write exactly what it prints — every line, in order. On paper, before any run. Then run it and compare.
"""

count = 0
for i in range(1, 4):
    for j in range(i):
        if j % 2 == 0:
            count = count + 1
    print(i, count)
print(count, i, j)

# The program prints four lines:
# 1 1
# 2 2
# 3 4
# 4 3 2

# count is initialised once, before the outer loop, so it never starts again for a new row.
# The last line reads the three names after the loops:
# count is 4, i is 3 (the last value range(1, 4) handed out),
# j is 2 (the last value range(3) handed out).

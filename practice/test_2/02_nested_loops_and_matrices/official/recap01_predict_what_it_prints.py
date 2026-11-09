"""Read the program below and write exactly what it prints — every line, in order.
On paper, before any run. Then run it and compare.
"""

count = 0
for i in range(1, 4):
    for j in range(i):
        if j % 2 == 0:
            count = count + 1
    print(i, count)
print(count, i, j)

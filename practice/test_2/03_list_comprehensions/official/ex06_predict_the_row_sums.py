"""Read the program below and write exactly the list it prints.
On paper, before any run. Then run it and compare."""

M = [[1, 2, 3], [40, 50, 60]]
sums = [row[0] + row[1] + row[2] for row in M]
print(sums)

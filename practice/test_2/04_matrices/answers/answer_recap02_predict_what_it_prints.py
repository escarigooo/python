"""Read the program below and write exactly what it prints — every line, in order.
On paper, before any run. Then run it and compare."""

row = [0, 0, 0]
A = [row, row]
B = [[0 for c in range(3)] for r in range(2)]
A[0][1] = 5
B[0][1] = 5
in_a = [v for r in A for v in r if v > 0]
in_b = [v for r in B for v in r if v > 0]
print(A, len(in_a))  # [[0, 5, 0], [0, 5, 0]] 2 - one row, stored twice
print(B, len(in_b))  # [[0, 5, 0], [0, 0, 0]] 1 - every row a list of its own

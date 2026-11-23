"""Write the comprehension that builds a grid of zeros with 4 rows and 5 columns, then print it.
Use this lecture’s nested comprehension — and check the shape with len(M) and len(M[0])
before you trust it: that check must print exactly what the output below shows."""

M = [[0 for c in range(5)] for r in range(4)]
print(M)
print(len(M), len(M[0]))  # 4 5

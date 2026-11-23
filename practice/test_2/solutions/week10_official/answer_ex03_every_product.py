"""Write the comprehension that builds the list of every product a × b, for a and b from 1 to 3, then print it — exactly as the output below shows. Use this lecture’s double comprehension: two for-clauses in one line."""

products = [a * b for a in range(1, 4) for b in range(1, 4)]
print(products)  # [1, 2, 3, 2, 4, 6, 3, 6, 9]

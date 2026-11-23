"""A 3-by-2 matrix typed by the user, element by element, built in one line."""

# the work
M = [[int(input(f"Element ({i}, {j}): ")) for j in range(2)] for i in range(3)]

# the answer
print(M)

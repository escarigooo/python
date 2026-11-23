"""Two nested loops and one append: a flat list of four pairs."""

# the data
pairs = []

# the work
for r in range(2):
    for c in range(2):
        pairs.append([r, c])

# the answer
print(pairs)

"""The four lines, taken apart: a 2-by-3 grid of pairs built with nested loops and append."""

pairs = []
for i in range(2):
    for j in range(3):
        pairs.append([i, j])
print(pairs)

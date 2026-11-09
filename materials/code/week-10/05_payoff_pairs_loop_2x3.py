"""The payoff: the same nested list in one line.
The expression first, the loop second,
in roder — from left to right."""

pairs = [[i, j] for i in range(2) for j in range(3)]
print(pairs)

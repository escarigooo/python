"""Build the list below twice, on paper, from range(1, 6).

The output to produce:
>>> [2, 4, 6, 8, 10]"""

# the loop
doubles = []
for n in range(1, 6):
    doubles.append(n * 2)
print(doubles)  # [2, 4, 6, 8, 10]

# the fold: the expression first, the for line after it, brackets around
doubles = [n * 2 for n in range(1, 6)]
print(doubles)  # the same [2, 4, 6, 8, 10]

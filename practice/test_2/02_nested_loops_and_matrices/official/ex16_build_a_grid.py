"""Read the program — today’s nested loops, now filling a list.
Predict the list it prints, then run it and compare.
Count the lines again.
"""

pairs = []
for i in range(3):
    for j in range(3):
        pairs.append((i, j))
print(pairs)

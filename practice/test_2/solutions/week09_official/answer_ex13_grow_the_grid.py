"""Start from the matrix in the panel.
First give the grid one more column: append a 0 to the end of every row.
Then give it one more row: append [0, 0, 0, 0].
Print the matrix after each of the two steps, exactly as the output shows — week 7’s append does both jobs.

The output to produce:
>>> [[7, 2, 9, 0], [4, 1, 5, 0], [3, 8, 6, 0]]
>>> [[7, 2, 9, 0], [4, 1, 5, 0], [3, 8, 6, 0], [0, 0, 0, 0]]
"""

m = [[7, 2, 9], [4, 1, 5], [3, 8, 6]]
for row in m:
    row.append(0)
print(m)  # [[7, 2, 9, 0], [4, 1, 5, 0], [3, 8, 6, 0]]
m.append([0, 0, 0, 0])
print(m)  # [[7, 2, 9, 0], [4, 1, 5, 0], [3, 8, 6, 0], [0, 0, 0, 0]]

# One more column touches every row, so it takes the loop;
# one more row is a single append, because a row is one item of m.

"""Each inner list of scores = [[7, 12, 5], [18, 3], [10, 10, 9, 14]] holds one group’s grades.
The program goes on with passed = … and ends with print(passed), which must show [1, 1, 3] —
how many grades of each group are 10 or higher.

One of A to G is right: pick it, and say what each of the others does instead."""

scores = [[7, 12, 5], [18, 3], [10, 10, 9, 14]]

# Uncomment one candidate at a time, run, and compare with the target.

# A
# passed = [len(row) for row in scores if row >= 10]

# B
# passed = [[s for s in row if s >= 10] for row in scores]

# C
# passed = [len([s for s in row if s > 10]) for row in scores]

# D
# passed = [len(s) for row in scores for s in row if s >= 10]

# E
# passed = [s for row in scores for s in row if s >= 10]

# F
# passed = [len([s for s in row if s >= 10]) for row in scores]

# G
# passed = [len(row) for row in scores]

print(passed)

# >>> [1, 1, 3]

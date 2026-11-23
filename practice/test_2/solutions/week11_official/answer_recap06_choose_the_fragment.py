"""Each inner list of scores = [[7, 12, 5], [18, 3], [10, 10, 9, 14]] holds one group’s grades.
The program goes on with passed = … and ends with print(passed), which must show [1, 1, 3] —
how many grades of each group are 10 or higher.

One of A to G is right: pick it, and say what each of the others does instead."""

scores = [[7, 12, 5], [18, 3], [10, 10, 9, 14]]

# A - TypeError: the filter compares a whole row with 10
# passed = [len(row) for row in scores if row >= 10]

# B - the grades themselves, not how many -> [[12], [18], [10, 10, 14]]
# passed = [[s for s in row if s >= 10] for row in scores]

# C - > leaves out the grades equal to 10 -> [1, 1, 1]
# passed = [len([s for s in row if s > 10]) for row in scores]

# D - TypeError: len of a number
# passed = [len(s) for row in scores for s in row if s >= 10]

# E - one flat list of the grades, the groups gone -> [12, 18, 10, 10, 14]
# passed = [s for row in scores for s in row if s >= 10]

# F - the right one
passed = [len([s for s in row if s >= 10]) for row in scores]

# G - counts every grade, with no test at all -> [3, 2, 4]
# passed = [len(row) for row in scores]

print(passed)  # [1, 1, 3]

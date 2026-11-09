"""Build the list below in one line from the list given in the panel, then print it. On paper, before any run. Use this lecture’s filter: an if after the for-clause.

The output to produce:
>>> [3, 7, 2]"""

nums = [3, -1, 7, -5, 2]

# the solution
positives = [n for n in nums if n > 0]
print(positives)  # [3, 7, 2]

"""Build the list below twice, on paper, from the strings "ab" and "xy". First with two nested for loops and append. Then fold your own loops into a comprehension with two for-clauses — same list, both ways.

The output to produce:
>>> ['ax', 'ay', 'bx', 'by']"""

# the loops
combos = []
for c1 in "ab":
    for c2 in "xy":
        combos.append(c1 + c2)
print(combos)  # ['ax', 'ay', 'bx', 'by']

# the fold: the expression first, the two for-clauses after it, in the same order
combos = [c1 + c2 for c1 in "ab" for c2 in "xy"]
print(combos)  # the same ['ax', 'ay', 'bx', 'by']

"""The filter works with two loops: the if comes last, after both for-clauses — the pairs that fail the test never enter."""

combos = [c1 + c2 for c1 in "ab" for c2 in "ab" if c1 != c2]
print(combos)

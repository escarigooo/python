"""Choose the fragment that prints a triangle of stars:
one star on the first row, two on the second, three on the third — each row on its own line.
One of A to D is right: pick it, and say what each of the others does instead.
"""

# A — the right fragment
for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()

# The fragment prints:
# *
# **
# ***

# B — the outer range(3) starts at 0, so the first row has no stars:
#     an empty line, then *, then **. It runs and lies.
# for i in range(3):
#     for j in range(i):
#         print("*", end="")
#     print()

# C — the bare print() is indented into the inner loop, so every star
#     ends its own line: six lines of one star each.
# for i in range(1, 4):
#     for j in range(i):
#         print("*", end="")
#         print()

# D — there is no print() after the inner loop, so nothing ever ends
#     a row: ****** on one line.
# for i in range(1, 4):
#     for j in range(i):
#         print("*", end="")

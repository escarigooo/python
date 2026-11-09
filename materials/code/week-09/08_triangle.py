"""The triangle: range(i) makes each row as long as the outer counter.
"""

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

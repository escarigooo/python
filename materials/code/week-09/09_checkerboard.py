"""The checkerboard: the if decides each cell from both counters.
"""

for i in range(10):
    for j in range(20):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

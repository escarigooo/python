"""Your turn: index_of_max hands back the position of the largest number in a list.
The given call, and one solution."""

# the function: best holds a position, not a value
def index_of_max(values):
    best = 0
    for i in range(1, len(values)):
        if values[i] > values[best]:
            best = i
    return best

# the given call
print(index_of_max([3, 9, 4, 9, 1]))

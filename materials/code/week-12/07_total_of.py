"""total_of with return: each call adds up its own total and hands the number back."""

# the definition
def total_of(M):
    total = 0
    for row in M:
        for value in row:
            total = total + value
    return total

# the main part
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(total_of(A), total_of(B))

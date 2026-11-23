"""The loop written once, under the name print_matrix, and called for A and for B."""

# the definition: written once, nothing runs here
def print_matrix(M):
    for row in M:
        print(row)

# the main part: two calls
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print_matrix(A)
print_matrix(B)

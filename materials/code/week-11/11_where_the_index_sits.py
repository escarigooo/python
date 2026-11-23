"""Reference only, not course material: the same two matrices, six index strings, six results (needs NumPy)."""

import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# the six rows of the slide's table, in order
print(np.einsum('ij,jk->ik', A, B).tolist())
print(np.einsum('ij,kj->ik', A, B).tolist())
print(np.einsum('ji,jk->ik', A, B).tolist())
print(np.einsum('ij,ij->', A, B).tolist())
print(np.einsum('ii->', A).tolist())
print(np.einsum('ij->ji', A).tolist())

# not on the slide: the row sums
print(np.einsum('ij->i', A).tolist())

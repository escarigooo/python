"""Write the function scale: it takes a matrix and a factor,
and hands back a new matrix with every element multiplied by the factor —
the matrix it was handed must stay as it was.
The three lines under the hole are given; the output below is what they must show.
One return, with week 11’s nested comprehension.

The output to produce:
>>> [[1, 2], [3, 4]] [[10, 20], [30, 40]]
"""

# your def here

A = [[1, 2], [3, 4]]
B = scale(A, factor=10)
print(A, B)

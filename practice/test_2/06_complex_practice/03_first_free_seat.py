"""Difficulty 4/5 - First free seat

The nested list represents seats. 1 means occupied and 0 means free. Print the row
and column of the first free seat in row-by-row reading order, then stop searching.
If no seat is free, print "full".

Expected output for the supplied grid:
first free seat: row 1, column 1

Use nested loops, a Boolean flag, and break. Remember: break exits only the loop in
which it appears, so the outer loop also needs a stopping condition.
"""

seats = [
    [1, 1, 1],
    [1, 0, 0],
    [0, 0, 1],
]

# TODO: Find only the first free seat.

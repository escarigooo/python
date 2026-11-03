"""EXERCISE 20 — Finding the largest value

Print the first zone with the largest count without using max().

For counts = [4, 9, 6, 9]
Expected output: Busiest: Central with 9 parcels

Correct the program. Explain the correct initial values, range boundaries, list
indexes, and comparison needed to keep the first result when counts are tied.
"""

zones = ["North", "Central", "South", "West"]
counts = [4, 9, 6, 9]
largest_count = 0
largest_index = 1

for index in range(1, len(counts) + 1):
    if counts[index] >= largest_count:
        largest_count = index
        largest_index = counts[index]

print(f"Busiest: {zones[largest_index]} with {largest_count} parcels")


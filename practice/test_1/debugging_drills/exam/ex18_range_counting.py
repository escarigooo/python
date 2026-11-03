"""EXERCISE 18 — Parallel lists and nested decisions

Count how many student numbers belong to each inclusive range.

For students = [100, 155, 205, 299, 450]
Expected output:
Room A: 2
Room B: 2
Room C: 1

Correct the range checks and list update. Explain every correction.
"""

rooms = ["Room A", "Room B", "Room C"]
starts = [100, 200, 300]
ends = [199, 299, 499]
counts = [0, 0, 0]
students = [100, 155, 205, 299, 450]

for student in students:
    for index in range(len(rooms)):
        if student > starts[index] and student < ends[index]:
            counts[index] + 1

for index in range(len(rooms) + 1):
    print(f"{rooms[index]}: {counts[index]}")


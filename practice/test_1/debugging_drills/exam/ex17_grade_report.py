"""EXERCISE 17 — Conversion, count, and average

Convert comma-separated grades to integers. Print the number of passing grades
(10 or higher) and the average of all grades.

For raw_grades = "8,10,14,18"
Expected output:
Passing: 3
Average: 12.5

Correct all faulty lines without using sum().
"""

raw_grades = "8,10,14,18"
grades = raw_grades.split(",")
passing = 0
total = 0

for grade in grades:
    total = total + grade
    if grade >= 10:
        passing = passing + 1

average = total / len(grades - 1)
print(f"Passing: {passing}")
print(f"Average: {average}")


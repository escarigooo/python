"""EXERCISE 6 — Combined condition

A valid test grade is between 0 and 20, including both endpoints.

For grade = 25
Expected output: Invalid grade

Correct the program and explain why its condition accepts every number.
"""

grade = 25

if grade >= 0 and grade <= 20:
    print("Valid grade")
else:
    print("Invalid grade")

# Needs to use and instead of or because it 's two conditions for the real validation 
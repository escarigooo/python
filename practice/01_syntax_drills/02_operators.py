"""Difficulty: 1/5 | Time: 5-10 min | Concepts: arithmetic, comparison, logic.

Create two integer variables. Print their sum, difference, product, normal division,
floor division, remainder, and first number raised to the second. Then print whether
the first is larger and whether both numbers are positive.

Success: the program produces nine labelled results.
"""

# Write your solution below without opening SYNTAX.md.
value1 = 10
value2 = 3

print("Sum:", value1 + value2)
print("Difference:", value1 - value2)
print("Product:", value1 * value2)
print(f"Normal division: {value1 / value2:.2f}")
print("Floor division:", value1 // value2)
print("Remainder:", value1 % value2)
print("First number raised to the second:", value1 ** value2)
print("Is the first number larger?", value1 > value2)
print("Are both numbers positive?", value1 > 0 and value2 > 0)
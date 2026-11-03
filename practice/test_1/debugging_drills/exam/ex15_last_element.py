"""EXERCISE 15 — Indexing and off-by-one errors

Print the first and last names in the list.

Expected output:
First: Ana
Last: Diana

Correct the program in two different ways: once using len(), and once using a
negative index. Explain why the original index is invalid.
"""

names = ["Ana", "Bruno", "Carla", "Diana"]
print(f"First: {names[0]}")
print(f"Last: {names[(len(names) - 1)]}")

# len gives us the number of elements, but it starts on 0, so we need to remove 1  
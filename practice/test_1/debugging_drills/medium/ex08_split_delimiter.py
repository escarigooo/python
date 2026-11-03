"""EXERCISE 8 — Splitting input

The text contains three names separated by semicolons. Print one name per line.

Expected output:
Ana
Bruno
Carla

Correct the program and explain the chosen delimiter.
"""

text = "Ana;Bruno;Carla"
names = text.split(";")

for name in names:
    print(name)

# To split we need to use the same element that is separating the string parts that we want
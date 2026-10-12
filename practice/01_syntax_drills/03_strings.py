"""Difficulty: 1/5 | Time: 10 min | Concepts: indexing, slicing, string methods.

Store a sentence of at least ten characters. Print its length, first character, last
character, first five characters, uppercase form, and a version with spaces replaced
by hyphens. Finally, check whether the word "Python" occurs in it.

Success: the program works for a different sentence after changing only one variable.
"""

# Write your solution below without opening SYNTAX.md.

# REVIEW: Correctly spelled and clearly named variable.
sentence = "Hello World !"

# REVIEW: Correct use of len() and an f-string.
print(f"{sentence} has a size of: {len(sentence)}")

# REVIEW: Correct indexes for the first and last characters.
# HINT: Add labels so the output explains what each character represents.
print(f"{sentence[0]}")
print(f"{sentence[-1]}")

# TODO: The exercise asks for the first five characters as one substring.
# HINT: Use a slice that starts at the beginning and stops before index 5.
for i in range(5):
    print(f"{sentence[i]}")

# REVIEW: Correct use of upper().
print(f"{sentence.upper()}")

# TODO: split() creates a list of words; it does not replace spaces.
# HINT: Use the string method that replaces an old value with a new value.
print(f"{sentence.split()}")

# TODO: Add the final requirement: check whether "Python" occurs in the sentence.
# HINT: Python has a membership operator that reads like an English word.

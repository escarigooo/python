"""Difficulty: 2/5 | Time: 15-20 min | Concepts: strings, for, membership, counter.

Week 6 handout - Exercise 7

Ask the user for a word. Count its consonants: letters that are not a, e, i, o,
or u. Print the final count.

Example: python produces 4.
"""

# HINT: Store all vowels together in one string.
# HINT: Normalize the word's capitalisation before checking its letters.
# Assume the user enters a word containing letters only.


word = input("Enter a word: ")
word = word.lower()

consonants = 0
for i in word:
    if i.lower() not in "aeiou":
        consonants += 1
print(consonants)
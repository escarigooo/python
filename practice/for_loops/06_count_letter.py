"""Difficulty: 2/5 | Time: 10-15 min | Concepts: input, for, if, counter.

Week 6 handout - Exercise 6

Ask the user for a word and one letter. Print how many times that letter appears
in the word.

Example: word = "banana" and letter = "a" produces 3.
"""

# STEP 1: Ask for the word and letter.
# STEP 2: Create a counter that starts at zero.
# STEP 3: Inspect every character and increase the counter after a match.
# STEP 4: Print the counter after the loop finishes.

word = input("Word: ")
letter = input("Letter: ")

i = 0
for j in word:
    if j == letter:
        i+=1
print(i)
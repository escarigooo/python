"""Course week(s): 07-08 | Difficulty: 2/5

Use while loops and a list to print the odd numbers from 1 through 9.

First, build a list containing 1, 3, 5, 7, and 9 with append(). Then use a
second while loop to print one list item per line. Do not use a for loop.
"""

numbers = []
number = 1

while number <= 9:
    numbers.append(number)
    number = number + 2

index = 0
while index < len(numbers):
    print(numbers[index])
    index = index + 1

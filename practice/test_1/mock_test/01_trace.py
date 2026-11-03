"""GROUP 1 — Predict the exact output without running this file.

Write the output exactly as Python prints it. Also write the type of every value
requested by a question.
"""


# QUESTION 1 — values, types, conversion, and operators
age_text = "20"
next_age = int(age_text) + 1
repeated = age_text * 2

print(next_age)
print(repeated)
print(type(next_age).__name__)
print(type(repeated).__name__)


# QUESTION 2 — string methods, len(), and Boolean expressions
name = "Ana-Maria"
clean_name = name.replace("-", "")
answer = len(clean_name) == 8 and name.startswith("A")

print(clean_name.lower())
print(answer)
print("Maria" in name)


# QUESTION 3 — list, for loop, conditions, counter, and accumulator
numbers = [3, 6, 2, 5]
changed = []
total = 0

for number in numbers:
    if number % 2 == 0:
        changed.append(number + 1)
        total = total + number
    else:
        total = total - number

print(changed)
print(total)
print(len(changed))


# QUESTION 4 — indexing, slicing, and range()
word = "programming"
values = [10, 20, 30, 40, 50]

print(word[1:8:2])
print(word[::-1][:4])
print(values[-4:-1])

for index in range(1, len(values), 2):
    print(values[index])


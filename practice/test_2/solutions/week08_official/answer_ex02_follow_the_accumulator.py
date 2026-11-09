"""Exercise 2 · Predict what it prints

Read the program below and write the number it prints, and how many turns the loop took.
On paper, then run it and compare.

total print 10 (1 + 2 + 3 + 4), in four turns (uncomment the print line inside the while to see each tur running)

"""
total = 0
i = 1
while i <= 4:
    # print(i)
    total = total + i
    i = i + 1
print(total)

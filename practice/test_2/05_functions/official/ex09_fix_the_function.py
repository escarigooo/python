"""average_above should hand back the average of the grades equal to or above the limit:
the program should print 12.0 and nothing else. It runs and raises nothing, yet it prints 26.0 and then None.
Three lines are to blame: find them, say what each one does, and write the fix.
"""

def average_above(grades, limit):
    total = 0
    for g in grades:
        count = 0
        if g > limit:
            total = total + g
            count = count + 1
    print(total / count)

result = average_above([12, 8, 10, 14], 10)
print(result)

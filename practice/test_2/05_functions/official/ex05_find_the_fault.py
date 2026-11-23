"""bigger should hand back the bigger of two numbers — and None when the two are equal.
The program should print two lines: 9, then None. It runs and raises nothing, yet it prints four: 9, None, 5 and None. Find what the function fails to do, and fix it.
"""

def bigger(a, b):
    if a > b:
        print(a)
    else:
        print(b)

result = bigger(4, 9)
print(result)
print(bigger(5, 5))

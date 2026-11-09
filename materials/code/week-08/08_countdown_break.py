"""The same countdown leaving early: the if checks the next step, break leaves before it overshoots."""
n = 10
while n > 0:
    print(n)
    if n - 3 < 0:
        break
    n = n - 3
print(n)

"""Reset 1: the countdown overshoots -- prints 10, 7, 4, 1, then the -2 it stopped on."""
n = 10
while n > 0:
    print(n)
    n = n - 3
print(n)

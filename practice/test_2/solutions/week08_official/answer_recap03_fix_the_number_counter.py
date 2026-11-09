"""Recap 3 · Debug

The program should ask for numbers until the user types 0, then print how many numbers were typed and their sum.
It runs, but it never stops — not even after a 0.
Find every line to blame, say why each one keeps the loop going, and write the fixes.
"""
total = 0
count = 0
# was: n = input("Number: ") — input returns text, and "0" != 0 is always True
n = int(input("Number: "))
while n != 0:
    total = total + n
    count = count + 1
    # was outside the loop, not indented — nothing inside moved the condition (trap 02)
    n = int(input("Number: "))
print(count, total)  # typing 4, 6, 0 prints 2 10

"""The program below should cut the string at the commas, keep the values above 10,
and print them with their sum: [18, 15] 33. The first run stops with an error;
fix it, and it prints the right list with a wrong sum. Find and fix both mistakes —
on paper, before any run. Then run it and confirm."""

text = "4,18,15,6"
nums = [int(n) for n in text.split()]
big = []
total = 0
for n in nums:
    if n > 10:
        big.append(n)
        total = total + 1
print(big, total)

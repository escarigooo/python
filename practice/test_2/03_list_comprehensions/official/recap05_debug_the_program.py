"""The program below should cut the string at the semicolons,
keep the names longer than three letters in upper case,
and print them with their count: ['GRACE', 'HOPPER'] 2.
The first run stops with an error — and fixing it is not the end.
Remember that a program that runs is not a program that is right.
Find and fix every mistake: on paper first, then run and compare."""

text = "ada;grace;hopper;ken"
names = text.split(",")
long = [n.upper for n in names if len(n) > 3]
count = 0
for n in long:
    count = count + n
print(long, count)

"""Expected output: ['GRACE', 'HOPPER'] 2.
The program has a delimiter error, a method-call error, and a counting error."""

text = "ada;grace;hopper;ken"
names = text.split(",")
long_names = [name.upper for name in names if len(name) > 3]
count = 0
for name in long_names:
    count = count + name
print(long_names, count)

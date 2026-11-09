"""Convert every piece at once: split() with no argument cuts on the spaces;
float() converts each piece as it comes in."""

text = "3.5 4.0 2.0"
numbers = [float(e) for e in text.split()]
print(numbers)

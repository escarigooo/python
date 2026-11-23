"""Write the comprehension that cuts the string at the commas and makes a list of ints, then print it — exactly as the output below shows. Start from the string given in the panel. Use this lecture’s comprehension, with split from week 4 — convert every element as it comes in."""

text = "10,20,30,40"
numbers = [int(e) for e in text.split(",")]
print(numbers)  # [10, 20, 30, 40]

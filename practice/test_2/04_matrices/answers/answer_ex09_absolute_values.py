"""Write the comprehension that turns the list given in the panel into the list of its absolute values,
then print it — exactly as the output below shows.
Use this lecture’s conditional expression inside the comprehension."""

nums = [5, -3, 8, -1]
absolutes = [n if n >= 0 else -n for n in nums]
print(absolutes)  # [5, 3, 8, 1]

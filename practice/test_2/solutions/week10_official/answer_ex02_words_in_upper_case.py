"""Write the comprehension that turns the list of words given in the panel into a new list with the words in upper case, then print it exactly as the output below shows. Use this lecture’s one-line form, with the string method from week 3."""

words = ["ada", "grace", "ken"]
caps = [w.upper() for w in words]
print(caps)  # ['ADA', 'GRACE', 'KEN']

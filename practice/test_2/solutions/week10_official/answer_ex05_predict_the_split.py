"""Read the program below and write exactly the list it prints, element by element, in order. On paper, before any run. Then run it and compare — everything in it is taught material, from week 4’s split to this lecture’s comprehension."""

text = "1,2;3,4"
rows = [p.split(",") for p in text.split(";")]
print(rows)  # [['1', '2'], ['3', '4']]
# A list of two lists, every element still a string — nothing converts, and the quotes are the tell.

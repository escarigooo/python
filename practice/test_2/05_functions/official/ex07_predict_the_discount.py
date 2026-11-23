"""Read the program below — the name price lives in two places.
On paper, before any run: write exactly the line it prints.
Then run it and compare.
"""

def discount(price, rate):
    price = price - price * rate / 100
    return price

price = 80
new = discount(price, 25)
discount(new, 50)
print(price, new)

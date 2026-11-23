"""return ends the function and hands exactly one value back to where the call was."""

# the definition
def add(a, b):
    result = a + b
    return result
    print("never runs")

# the main part
x = 5
y = 3
z = add(x, y)
print(z)

"""Exercise 10 resolved: break stops the search at the first negative."""
values = [4, 7, -2, 9, -5]
for i in range(len(values)):
    if values[i] < 0:
        print("Negative at", i)
        break

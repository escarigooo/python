"""The expression may compute with both variables: 10 * r + c — the tens from r, the units from c."""

my_list = [10 * r + c for r in range(3) for c in range(3)]
print(my_list)

"""The intention is to add 30 only to copy_values, leaving values as [10, 20].
Both lists change. Explain aliasing and correct the copy line."""

values = [10, 20]
copy_values = values
copy_values.append(30)
print(values)
print(copy_values)

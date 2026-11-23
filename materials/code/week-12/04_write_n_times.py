"""A function with two parameters: what to print, and how many times."""

# the definition
def write_n_times(s, n):
    for i in range(n):
        print(s)

# the main part: two calls, two different jobs
write_n_times("hi", 2)
write_n_times("go", 3)

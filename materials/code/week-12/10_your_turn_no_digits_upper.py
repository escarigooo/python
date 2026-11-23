"""Your turn: no_digits_upper hands back the text in upper case, with every digit left out.
The given call, and one solution."""

# the function: a new string, built letter by letter
def no_digits_upper(text):
    result = ""
    for ch in text:
        if not ch.isdigit():
            result = result + ch.upper()
    return result

# the given call
print(no_digits_upper("py3thon12"))

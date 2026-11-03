"""GROUP 3 — Replace every TODO with working Python.

Do not use sum(), max(), min(), list comprehensions, while loops, or topics taught
after Week 7. Complete the functions using conversions, lists, conditions, and for
loops.
"""


def analyse_numbers(raw_numbers):
    """Return [converted_numbers, total, even_count].

    Example:
        analyse_numbers("3,8,5,2") -> [[3, 8, 5, 2], 18, 2]
    """
    parts = ...  # TODO 1: split raw_numbers at each comma
    numbers = []
    total = 0
    even_count = 0

    for part in parts:
        number = ...  # TODO 2: convert part to an integer
        ...  # TODO 3: append number to numbers
        ...  # TODO 4: add number to total

        if ...:  # TODO 5: check whether number is even
            ...  # TODO 6: increase even_count

    return [numbers, total, even_count]


def normalise_names(raw_names):
    """Return cleaned lowercase names.

    Names are separated by semicolons. Remove spaces and hyphens from each name.
    Example:
        normalise_names("Ana Silva;Joao-Pedro")
        -> ["anasilva", "joaopedro"]
    """
    names = ...  # TODO 7: separate the names
    cleaned_names = []

    for name in names:
        cleaned = ...  # TODO 8: remove spaces
        cleaned = ...  # TODO 9: remove hyphens
        cleaned = ...  # TODO 10: make it lowercase
        ...  # TODO 11: store it in cleaned_names

    return cleaned_names


def largest_value(values):
    """Return the largest number without using max()."""
    largest = ...  # TODO 12: begin with the first list element

    for value in values:
        if ...:  # TODO 13: decide whether value is a new largest value
            ...  # TODO 14: update largest

    return largest


# Run these checks only after filling every blank.
print(analyse_numbers("3,8,5,2"), "EXPECTED: [[3, 8, 5, 2], 18, 2]")
print(normalise_names("Ana Silva;Joao-Pedro"), "EXPECTED: ['anasilva', 'joaopedro']")
print(largest_value([-8, -2, -11, -3]), "EXPECTED: -2")


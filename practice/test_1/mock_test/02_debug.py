"""GROUP 2 — Correct each function and explain every error on paper first.

All four functions run, but they produce an incorrect result. Do not redesign the
whole function. Correct the faulty lines using Weeks 1-7 syntax.
"""


def make_username(full_name):
    """Return the lowercase name with spaces and hyphens removed."""
    username = full_name.lower
    username.replace(" ", "")
    username.replace("-", "")
    return username


def count_passing_grades(grades):
    """Return how many grades are greater than or equal to 10."""
    count = 0
    for index in range(1, len(grades)):
        if grades[index] >= 10:
            count + 1
    return count


def double_prices(prices):
    """Change every price in the original list to twice its value."""
    for price in prices:
        price = price * 2
    return prices


def words_longer_than(text, minimum):
    """Return a list containing words longer than minimum."""
    selected = []
    words = text.split

    for index in range(len(words) + 1):
        if len(words[index]) > minimum:
            selected = selected.append(words[index])

    return selected


# Run these only after making all your corrections.
print(make_username("Ana Maria-Silva"), "EXPECTED: anamariasilva")
print(count_passing_grades([9, 10, 15, 7, 12]), "EXPECTED: 3")
print(double_prices([2, 4, 6]), "EXPECTED: [4, 8, 12]")
print(words_longer_than("one three seven two", 3), "EXPECTED: ['three', 'seven']")


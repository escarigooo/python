"""A complete Python syntax tour built as a student-grade report.

This example combines variables, types, input, conversion, strings, arithmetic,
comparisons, Boolean logic, conditions, lists, loops, functions, validation,
exceptions, list comprehensions, and formatted output.

Run it with:
    python3 examples/student_report.py
"""

# Constants use uppercase names by convention.
MINIMUM_GRADE = 0.0
MAXIMUM_GRADE = 20.0
PASSING_GRADE = 10.0


def read_positive_integer(prompt):
    """Keep asking until the user enters a positive integer."""
    while True:
        text = input(prompt).strip()

        if text.isdigit():
            number = int(text)
            if number > 0:
                return number

        print("Please enter a positive whole number.")


def read_grade(prompt):
    """Keep asking until the user enters a number from 0 through 20."""
    while True:
        text = input(prompt).strip()

        try:
            grade = float(text)
        except ValueError:
            print("Please enter a number, such as 14 or 16.5.")
            continue

        if MINIMUM_GRADE <= grade <= MAXIMUM_GRADE:
            return grade

        print(f"The grade must be between {MINIMUM_GRADE} and {MAXIMUM_GRADE}.")


def calculate_average(numbers):
    """Return the arithmetic average of a non-empty list of numbers."""
    return sum(numbers) / len(numbers)


def classify_average(average):
    """Return a description for an average grade."""
    if average >= 18:
        return "Excellent"
    elif average >= 14:
        return "Good"
    elif average >= PASSING_GRADE:
        return "Passed"
    else:
        return "Failed"


def print_report(name, student_number, course, grades):
    """Calculate and display the complete student report."""
    average = calculate_average(grades)
    highest_grade = max(grades)
    lowest_grade = min(grades)
    classification = classify_average(average)
    passed = average >= PASSING_GRADE

    # A list comprehension creates a new list using a condition.
    passing_grades = [grade for grade in grades if grade >= PASSING_GRADE]

    print("\n" + "=" * 40)
    print("STUDENT REPORT")
    print("=" * 40)
    print(f"Name: {name}")
    print(f"Student number: {student_number}")
    print(f"Course: {course}")
    print(f"Name length: {len(name)} characters")

    print("\nGrades:")
    for position, grade in enumerate(grades, start=1):
        print(f"  Grade {position}: {grade:.1f}")

    print(f"\nAverage: {average:.2f}")
    print(f"Highest: {highest_grade:.1f}")
    print(f"Lowest: {lowest_grade:.1f}")
    print(f"Passing grades: {len(passing_grades)} of {len(grades)}")
    print(f"Classification: {classification}")

    if passed and lowest_grade >= PASSING_GRADE:
        print("Result: Passed every assessment")
    elif passed:
        print("Result: Passed overall, but failed at least one assessment")
    else:
        print("Result: Failed overall")


def main():
    """Collect the input and coordinate the program."""
    print("Student grade report\n")

    # String methods clean and format the user's text.
    name = input("Student name: ").strip().title()
    student_number = input("Student number: ").strip()
    course = input("Course name: ").strip().title()

    number_of_grades = read_positive_integer("Number of grades: ")
    grades = []

    # range stops before its second value, so +1 includes number_of_grades.
    for position in range(1, number_of_grades + 1):
        grade = read_grade(f"Grade {position}: ")
        grades.append(grade)

    print_report(name, student_number, course, grades)


# Run main only when this file is executed directly.
if __name__ == "__main__":
    main()

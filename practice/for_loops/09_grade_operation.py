"""Difficulty: 3/5 | Time: 20-25 min | Concepts: input, validation, nested branching.

Week 6 handout - Exercise 9

Ask for two grades from 0 through 20. If either is outside the interval, print
an error. Otherwise, ask for "Average" or "Greatest" and print the requested
result.
"""

# STEP 1: Read both grades as numbers.
# STEP 2: Validate both before requesting the operation.
# STEP 3: Normalize and check the operation text.
# STEP 4: Calculate only the selected result.

grade_1 = float(input("Grade 1 (0-20): "))

if grade_1 <= 0 or grade_1 >= 20:
    print("Error: Grade 1 is out of range.")
else:    
    grade_2 = float(input("Grade 2 (0-20): "))

    if grade_2 <= 0 or grade_2 >= 20:
        print("Error: Grade 2 is out of range.")
    else:
        # TODO: Normalize this with strip() and lower() so spaces and capitals do
        # not make a correct choice fail.
        requested = input("Average or Greatest: ")
        if requested == "Average":
            # REVIEW: Correct average calculation.
            print((grade_1 + grade_2)/2)
        else:
            # ERROR: Every other word currently enters this branch. For example,
            # "hello" incorrectly prints the greatest grade.
            # TODO: Use elif for "Greatest", then add an else for an invalid choice.
            # STYLE: Python does not require parentheses around an if condition.
            if(grade_1 > grade_2):
                print(grade_1)
            else:
                print(grade_2)

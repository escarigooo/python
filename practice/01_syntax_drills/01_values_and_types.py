"""Difficulty: 1/5 | Time: 5-10 min | Concepts: variables, types, print.

Create variables containing your name, age, height, and whether you are a student.
Print each value and its type. Finish with one formatted sentence containing all four
values.

Success: the program prints four type names and one readable sentence.
"""

# Personal information
name = "André"
age = 18
height = 168.5
student_status = True

# Each value and its Python type
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Student status:", student_status, "| Type:", type(student_status))

# One formatted sentence containing all four values
print(
    f"{name} is {age} years old, is {height} cm tall, "
    f"and has a student status of {student_status}."
)

"""Difficulty: 3/5 | Time: 20-30 min | Concepts: input, Boolean logic, nested conditions.

Week 6 handout - Exercise 10

Ask for a department and years worked. Bonus rules:
- software or management: 30% with 3+ years, otherwise 25%
- finance: 20% with 5+ years, otherwise 15%
- maintenance: always 10%

Print the applicable bonus.
"""

# STEP 1: Read the department and years.
# STEP 2: Normalize the department's capitalisation.
# STEP 3: Choose the department rule, then apply any experience threshold.
# STEP 4: Print the selected percentage.
depart = input("Department: ")
years = int(input("Years: "))


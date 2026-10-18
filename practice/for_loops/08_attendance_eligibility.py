"""Difficulty: 3/5 | Time: 20-25 min | Concepts: input, percentage, conditions.

Week 6 handout - Exercise 8

Ask for the number of classes held, classes attended, and whether there is a
medical cause ("Y" or "N"). A student cannot sit the exam below 75% attendance
unless they have a medical cause. Print the percentage and the decision.
"""

# input() returns text, so convert both class counts to integers immediately.
classes_held = int(input("Number of classes held: "))
classes_attended = int(input("Number of classes attended: "))

# These methods allow answers such as "y", "Y", or " y ".
medical_cause = input("Medical cause? (Y/N): ").strip().upper()

# Validate the values before dividing. This prevents impossible attendance numbers
# and division by zero.
if classes_held <= 0:
    print("The number of classes held must be greater than zero.")
elif classes_attended < 0 or classes_attended > classes_held:
    print("Classes attended must be between zero and the classes held.")
elif medical_cause not in ("Y", "N"):
    print('Medical cause must be "Y" or "N".')
else:
    attendance_percentage = classes_attended / classes_held * 100

    # A student needs sufficient attendance OR a medical exemption.
    if attendance_percentage >= 75 or medical_cause == "Y":
        if attendance_percentage < 75:
            print(
                f"Percentage is {attendance_percentage:.1f}% with medical cause, "
                "you CAN attend the exam."
            )
        else:
            print(
                f"Percentage is {attendance_percentage:.1f}%, "
                "you CAN attend the exam."
            )
    else:
        print(
            f"Percentage is {attendance_percentage:.1f}%, "
            "you CANNOT attend the exam."
        )

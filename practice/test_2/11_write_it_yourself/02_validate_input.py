"""Course week(s): 04-05, 08 | Difficulty: 2/5

Keep asking for an integer from 1 through 5 until the input is valid.

Assume the user types an integer each time. Convert every input to int before
comparing it. When the number is valid, print "accepted".

Example: inputs 8, 0, 4 should print "accepted" after the third input.
"""

# TODO: Write your solution here.

'''ask int from 1-5
until input valid
receive value, convert to int
if valid, accept

'''

def ask_value(value):
    if int(value) >= 1  and int(value) <= 5:
        return "accepted"
    else:
        return "try again"

r_value = ""
while r_value != "accepted":
    r_value = ask_value(input("tell us your value: "))
    print(r_value)

"""Exercise 5 · Ask until the answer is yes

Write a program that keeps asking Continue? until the user types exactly yes, then prints ok.
Use this lecture’s while — the question itself is the condition.
One run of the finished program, for example:

Continue? no
Continue? maybe
Continue? yes
ok
"""
answer = input("Continue? ")
while answer != "yes":
    answer = input("Continue? ")
print("ok")

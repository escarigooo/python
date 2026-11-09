"""Exercise 9 · A program that chats

Write a program that chats: it greets the user, then keeps reading answers with input until the user types bye,
and then says goodbye. Pick two or three words to react to: when an answer contains one of them (week 3’s in),
reply with a matching question; otherwise reply with one neutral line that keeps the conversation going.

Use this lecture’s while — the length of the conversation is the user’s choice, not yours.

One run of the finished program, for example:
Hello, traveller. Where would you like to go?
> a quiet beach in the Algarve
Sun and sea! Which beach?
> maybe the mountains in winter
Fresh air! Hiking or skiing?
> bye
Goodbye, and have a good trip!
"""
print("Hello, traveller. Where would you like to go?")
answer = input("> ")
while answer != "bye":
    if "beach" in answer:
        print("Sun and sea! Which beach?")
    elif "mountain" in answer:
        print("Fresh air! Hiking or skiing?")
    else:
        print("Sounds nice! Tell me more.")
    answer = input("> ")
print("Goodbye, and have a good trip!")

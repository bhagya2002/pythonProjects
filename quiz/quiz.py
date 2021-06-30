# this a quiz game

# import question class
from Question import Question

# list of question
questions = [
    "What does CPU stand for?"
]


play = input("Do you want to play this game? ")

if play.lower() != "yes":
    quit()

print("Oki let's play :)")

for question in questions:


if answer == "central processing unit":
    print("correct!")
else:
    print("incorrect!")
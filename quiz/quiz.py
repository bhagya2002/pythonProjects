from Question import Question

# list of question
question_prompts = [
    "What does CPU stand for? ",
    "What does GPU stand for? ",
    "What does RAM stand for? ",
    "What does PSU stand for? ",
]

questions = [
    Question(question_prompts[0], "central processing unit"),
    Question(question_prompts[1], "graphics processing unit"),
    Question(question_prompts[2], "random access memory"),
    Question(question_prompts[3], "power supply unit"),
]


play = input("Do you want to play this game? ")

if play.lower() != "yes":
    quit()

print("Oki let's play :)")


def play_game(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)

        if answer.lower() == question.answer:
            score += 1
            print("correct!")
        else:
            print("incorrect!")

    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")


play_game(questions)

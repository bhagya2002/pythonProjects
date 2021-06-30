# imports
import random

# user picks upper boundry
top_of_range = input("Type a number: ")

# data validation
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time!")
        quit()
else:
    print("Please enter a number next time!")
    quit()

# randrange does not include right end
# randint does include right
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    # user makes a guess
    user_guess = input("Make a guess: ")

    # user makes a guess
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time!")
        # brings to the top of the loop again
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You guessed higher than the secret number.")
    else:
        print("You guessed lower than the secret number.")

print("You got it in", guesses, "guesses")

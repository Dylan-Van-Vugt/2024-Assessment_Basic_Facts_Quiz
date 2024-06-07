import random


def string_checker(question, valid_ans=('yes', 'no')):
    error = f"\nPlease enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # Check if the user response is a word in the list
            if item == user_response:
                return item

            # Check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # Print error if user does not enter a valid answer
        print(error)
        print()


# Checks that users enter an integer that is more than 1

def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # Check for inf mode
        if to_check == "":
            return ""

        try:
            response = int(to_check)

            # checks that the number is more than 1
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Variables
questions_answered = 0
questions_correct = 0
questions_incorrect = 0
mode = 'none'

game_history = []

# Start
num_rounds = int_check("How many rounds would you like to play? Press <enter> for infinite mode: ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

while questions_answered < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n **  Round {questions_answered + 1} (Infinite Mode)  ** "
    else:
        rounds_heading = f"\n **  Round {questions_answered + 1} of {num_rounds}  ** "

    print(rounds_heading)
    print()

    testing_list = ['Correct', 'Incorrect']
    for item in range(0, 2):
        result = random.choice(testing_list)

    # Print results and add 1 to rounds played
    if result == "Correct":
        questions_correct += 1
        feedback = " ** You got it Correct! ** "
    else:
        feedback = " ** You got it Incorrect ** "
        questions_incorrect += 1

    question_feedback = f"{feedback}"
    history_item = f"Round: {questions_answered + 1} - {question_feedback}"

    print(question_feedback)
    game_history.append(history_item)

    questions_answered += 1

    # If users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

    # Make sure for testing that inf doesn't go inf
    if questions_answered == 25:
        break

# History

if questions_answered > 0:
    questions_correct = questions_answered - questions_incorrect
    percent_correct = questions_correct / questions_answered * 100
    percent_incorrect = questions_incorrect / questions_answered * 100

    print()
    print()
    print(" ***  Game Stats  *** ")
    print(f" * Won: {percent_correct:.2f}% * \t "
          f" * Lost: {percent_incorrect:.2f}% * \t ")
    print()

    show_history = string_checker("Do you want to see the game history? ")
    if show_history == "yes":
        print("\n *** Game History *** ")

        for item in game_history:
            print(item)

        print()

else:
    print(" *** Oops - You chickened out! *** ")

    # When imported into full game make sure user can xxx

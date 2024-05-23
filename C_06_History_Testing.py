import random


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
rounds_played = 0
questions_correct = 0
questions_incorrect = 0
mode = 'none'

game_history = []

# Start
num_rounds = int_check("How many rounds would you like to play? Press <enter> for infinite mode: ")

if num_rounds == "":
    game_mode = "infinite"
    num_rounds = 5

while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n **  Round {rounds_played + 1} (Infinite Mode)  ** "
    else:
        rounds_heading = f"\n **  Round {rounds_played + 1} of {num_rounds}  ** "

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
    history_item = f"Round: {rounds_played + 1} - {question_feedback}"

    print(question_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # If users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

    # When imported into full game make sure user can xxx

import random


# Instructions
def instructions():
    print('''

*** Instructions ***

To begin, choose the amount of questions you want (or choose infinite mode).

Answer as many questions correctly as you can.
Then you can see the history of the game and see how well you did. 

Answer <xxx> to end the game at any time.

Good Luck
    ''')


# Checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks users enter yes (y) or no (n)
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not chose a valid response")


# Integer checker for integer more than 1
def int_check(question, low=None, exit_code=None):
    error = f"Please enter an integer that is one or more"

    while True:

        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response
        if response == "":
            return ""

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # if the response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# Print Title
print()
print(" ***  BEDMAS Quiz  *** ")
print()

# Ask if users want to see instructions
want_instructions = yes_no("Do you want to read the instructions? ")
if want_instructions == "yes":
    instructions()

print()

# Initialise Variables
a = 0
b = 0
c = 0
ans = 0
questions_answered = 0
questions_correct = 0
questions_incorrect = 0
mode = 'none'

quiz_history = []

# Start the main code
# Start Questions
num_questions = int_check("How many questions would you like to answer? Press <enter> for infinite mode: ",
                          low=1)

# Set up inf mode
if num_questions == "":
    mode = "infinite"
    num_questions = 5

# Main Game loop
while questions_answered < num_questions:

    # Rounds headings
    if mode == "infinite":
        questions_heading = f"\n **  Round {questions_answered + 1} (Infinite Mode)  ** "
    else:
        questions_heading = f"\n **  Round {questions_answered + 1} of {num_questions}  ** "

    print(questions_heading)
    print()

    # The questions and answering correctly

    # Initialise Variables
    add_operator = '+'
    subtract_operator = '-'
    multiply_operator = '*'
    divide_operator = '/'

    # Lists
    operator_list = [add_operator, subtract_operator, multiply_operator, divide_operator]
    abc_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Number of numbers
    num_numbers = random.choice([2, 3])

    print(num_numbers)

    # Set operators
    operator_1 = random.choice(operator_list)
    operator_2 = random.choice(operator_list)

    print(f"Operator 1 = {operator_1}, Operator 2 = {operator_2}")

    # Set numbers
    a = random.choice(abc_list)
    b = random.choice(abc_list)
    c = random.choice(abc_list)

    # Testing
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

    print(f"Operator 1 = {operator_1}, Operator 2 = {operator_2}")

    # Makes sure that there can not be 2 divisions and that all divisions equal a whole number
    if operator_1 or operator_2 == '/':
        if operator_1 and operator_2 == '/':
            operator_1 = random.choice(operator_list)
            operator_2 = random.choice(operator_list)
        if operator_2 == '/':
            b = b * c
        if operator_1 == '/':
            a = a * b

    # Math
    print(eval(f"{a} {operator_1} {b} {operator_2} {c}"))

    # Enter your answer

    ans = int_check(f"{a} {operator_1} {b} {operator_2} {c} = ",
                    exit_code="xxx")

    print(ans)

    if ans == "xxx":
        break

    # Answer
    if ans == eval(f"{a} {operator_1} {b} {operator_2} {c}"):
        result = "Correct"
    else:
        result = "Incorrect"

    # Now make it 2 and maybe let the user choose how many

    # Print results and add 1 to rounds played
    if result == "Correct":
        questions_correct += 1
        feedback = " ** You got it Correct! ** "
    else:
        feedback = " ** You got it Incorrect ** "
        questions_incorrect += 1

    # Get history
    question_feedback = f"{feedback}"
    history_item = f"Round: {questions_answered + 1} - {question_feedback}"

    print(question_feedback)
    quiz_history.append(history_item)

    print()

    questions_answered += 1

    # If users are in infinite mode, increase number of questions
    if mode == "infinite":
        num_questions += 1

    # Make sure for testing that inf doesn't go inf
    if questions_answered == 25:
        break

# History
if questions_answered > 0:
    questions_correct = questions_answered - questions_incorrect
    percent_correct = questions_correct / questions_answered * 100
    percent_incorrect = questions_incorrect / questions_answered * 100

    # Game Stats
    print()
    print()
    print(" ***  Quiz Stats  *** ")
    print(f" * Won: {percent_correct:.2f}% * \t "
          f" * Lost: {percent_incorrect:.2f}% * \t ")
    print()

    # Game History
    show_history = yes_no("Do you want to see the quiz history? ")
    if show_history == "yes":
        print("\n *** Quiz History *** ")

        for item in quiz_history:
            print(item)

        print()

    print(f" * Won: {percent_correct:.2f}% * \t "
          f" * Lost: {percent_incorrect:.2f}% * \t ")

else:
    print(" *** Oops - You chickened out! *** ")


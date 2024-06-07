print()


# Instructions
def instructions():
    print('''
*** Instructions ***

To begin, choose the amount of questions you want (or choose infinite mode).

Answer as many questions correctly as you can.
Then you can see the history of the game and see how well you did. 

Press <xxx> to end the game at any time.

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


# Ask if users want to see instructions
want_instructions = yes_no("Do you want to read the instructions? ")
# If yes print the instructions
if want_instructions == "yes":
    instructions()

print("Program Continues - ")
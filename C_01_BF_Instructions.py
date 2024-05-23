# Instructions
def instructions():
    print('''

*** Instructions ***

To begin, choose the amount of questions you want (or choose infinite mode).

Answer as many questions correctly as you can.
Then you can see the history of the game and see  how well you did. 

Press <xxx> to end the game at any time.

Good Luck
    ''')


# Main Routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# loop for testing purposes
while True:

    want_instructions = string_checker("Do you want to read the instructions? ")

    # checks users enter yes (y) or no (n)
    if want_instructions == "yes":
        instructions()

    print("program continues")

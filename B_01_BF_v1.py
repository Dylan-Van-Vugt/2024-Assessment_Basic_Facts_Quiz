import random


# Initialise variables
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


def instructions():
    print('''
*** Instructions ***

To begin, choose the amount of questions you want (or choose infinite mode).

Answer as many questions correctly as you can.
Then you can see the history of the game and see  how well you did. 

Press <xxx> to end the game at any time.

Good Luck

    ''')


# Quiz starts here
print()
print(" ***  Basic Facts Quiz  *** ")
print()

# Initialize variables
questions_played = 0
questions_correct = 0
questions_incorrect = 0
num_questions = 0
a = 0
b = 0
c = 0
ans = 0
question = 0
action_1 = '+'
action_2 = '-'
action_3 = '*'
action_4 = '/'

# Initialise Lists
abc_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
actions_list = [action_1, action_2, action_3, action_4]

# Instructions
want_instructions = yes_no("Do you want to read the instructions: ")

# Checks if they want instructions
if want_instructions == "yes":
    instructions()

# Initialise Questions
num_questions = input("How many rounds do you want to play (press <enter> for infinite mode): ")
if num_questions == "":
    num_questions = "infinite"

print(num_questions)

# Start rounds loop

# Initialize variables


for item in range(0, 9):
    a = random.choice(abc_list)
    b = random.choice(abc_list)
    c = random.choice(abc_list)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

for item in range(0, 1):
    action_1 = random.choice(actions_list)
    action_2 = random.choice(actions_list)

    print(f"Action 1 = {action_1}, Action 2 = {action_2}")

# Math
print(eval(f"{a} {action_1} {b} {action_2} {c}"))

ans = int(input(f"{a} {action_1} {b} {action_2} {c} = "))

print(ans)
# answer that never works

if ans == eval(f"{a} {action_1} {b} {action_2} {c}"):
    print("Yes")
else:
    print("no")

# Now make it 2 and maybe let the user choose how many

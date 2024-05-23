# Checks that users enter an integer that is more than 1

def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # Check for inf mode
        if to_check == "":
            return "infinite"

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
rounds_played = int(0)
rounds_won = int(0)
rounds_lost = int(0)

# Start
num_rounds = int_check("How many rounds would you like to play? Press <enter> for infinite mode: ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5
print(num_rounds)



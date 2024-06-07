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


# Testing
while True:

    print()

    yes_no_test = yes_no("Answer this question: ")

    print()

    if yes_no_test == "yes":
        print("You Chose Yes")
    else:
        print("You Chose No")
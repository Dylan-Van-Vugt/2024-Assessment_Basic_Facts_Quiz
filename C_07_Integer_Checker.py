# Checks that users enter an integer that is more than 1

def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # Check for inf mode
        if to_check == "":
            return "infinite"

        try:
            response = int(input("Enter an integer: "))

            # checks that the number is more than 1
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine goes here
target_score = int_check()
print(target_score)

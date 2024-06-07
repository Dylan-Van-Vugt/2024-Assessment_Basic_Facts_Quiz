# Checks that users enter an integer that is more than 1

# Integer checker for integer more than 1 with boundaries for rounds and for ans
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


# Variables for testing
a = 1
b = 2
c = 3

operator_1 = "+"
operator_2 = "-"

# Setting ans to what you think is the ans
ans = int_check(f"{a} {operator_1} {b} {operator_2} {c} = ",
                exit_code="xxx")


# Make sure users can exit the loop by pressing xxx
if ans == "xxx":
    print("The code ends")
else:
    print("Program Continues")






import random

# def int_check(question):

    # while True:
        # error = "Please enter an integer"

        # try:
          #   response = int(input(question))



# Variables
a = 0
b = 0
c = 0
ans = 0
question = 0

# List
a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for item in range(0, 9):
    a = random.choice(a_list)
for item in range(0, 9):
    b = random.choice(b_list)
for item in range(0, 9):
    c = random.choice(c_list)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


# Variables
action_1 = '+'
action_2 = '-'
action_3 = '*'
action_4 = '/'

# List
action_list_1 = [action_1, action_2, action_3, action_4]
action_list_2 = [action_1, action_2, action_3, action_4]

for item in range(0, 1):
    print_action_1 = random.choice(action_list_1)
    print_action_2 = random.choice(action_list_2)

    print(f"Action 1 = {print_action_1}, Action 2 = {print_action_2}")

# Math
print(eval(f"{a} {print_action_1} {b} {print_action_2} {c}"))

ans = int(input(f"{a} {print_action_1} {b} {print_action_2} {c} = "))

print(ans)
# answer that never works

if ans == eval(f"{a} {print_action_1} {b} {print_action_2} {c}"):
    print("Yes")
else:
    print("no")

#Now make it 2 and maybe let the user choose how many








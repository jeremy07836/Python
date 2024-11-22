import random


def get_integer(prompt="Enter integer: "):
    """
    Get an integer from Standard Input (stdin).

    The function will loop until a valid `int` is entered
    :param prompt: The prompt value for the stdin function
    :return: The integer the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("{} is not a valid number".format(temp))


highest = 10
answer = random.randint(1, highest)
print(answer)

print("Please guess the number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = get_integer()
    if guess == 0:
        print("Quitting")
        break
    elif guess == answer:
        print("Well done")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")


#####################################################################
#####################################################################
# old code
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("Wrong")
# else:
#     print("Correct")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Correct")
#     else:
#         print("Wrong")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Correct")
#     else:
#         print("Wrong")
# else:
#     print("Correct")

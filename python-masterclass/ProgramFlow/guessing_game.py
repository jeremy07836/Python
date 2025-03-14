import random


def get_integer(prompt, upper_limit):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            if 0 < int(temp) <= upper_limit:
                return int(temp)
            else:
                print("This is not a valid number between 1 and {}"
                      .format(upper_limit))
        else:
            print("This is not a number")


highest = 10
answer = random.randint(1, highest)
print(answer)

print("Please guess the number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = get_integer(": ", highest)

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

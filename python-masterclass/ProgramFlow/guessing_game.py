answer = 5

print("Please guess the number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("Well done")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess != answer:
        print("Wrong")
    else:
        print("Correct")

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

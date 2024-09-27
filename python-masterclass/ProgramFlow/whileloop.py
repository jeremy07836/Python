# for i in range(10):
#     print("i is now {}".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

message = "Please choose your option from the list below\n"\
          "1. Learn Python\n"\
          "2. Learn Java\n"\
          "3. Go swimming\n"\
          "4. Have dinner\n"\
          "5. Got to bed\n"\
          "0. Exit"

print(message)

choices = [1, 2, 3, 4, 5, 0]
choose = -1
while choose != 0:
    choose = int(input("Enter a number from the list "))
    if choose in choices:
        print("Selected from list {}".format(choose))
    else:
        print("Incorrect")
        print(message)
else:
    print("Exited program")

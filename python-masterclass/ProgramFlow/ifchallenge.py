name = input("What is your name? ")
age = int(input("What is your age? "))

if 18 <= age <= 30:
    print("Welcome to the holiday {}".format(name))
else:
    print("No holiday")

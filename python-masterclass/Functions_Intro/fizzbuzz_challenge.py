def fizz_buzz(n: int) -> str:
    """
    Returns string if the number is divisible by 3 or 5, otherwise
    it returns the number
    :param n: integer
    :return: a string or number
    """
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


# for number in range(1, 10 + 1):
#     fb = fizz_buzz(number)
#     print(fb)

player = 1
number = 1
while True:
    fb = fizz_buzz(number)
    print("Is {} divisible by 3 or 5:".format(number))
    guess = input("Fizz Buzz: ")
    guess = str(guess).casefold()
    if fb == guess:
        print("Correct")
        if player == 1:
            player = 2
        else:
            player = 1
    else:
        break
    number += 1

print("Game over Player {} loses".format(player))

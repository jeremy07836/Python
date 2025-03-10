LOW = 1
# HIGH = 1000
HIGH = 1023

# print("Please think of a number between {} and {}".format(low, high))
# input("Press ENTER to Continue: ")


def guess_binary(answer, low, high):
    # guess = 1
    guesses = 1
    while True:
        # print("\tGuessing in the range of {} to {}".format(low, high))
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower?\n"
        #                 "Enter h or l, or c if my guess was correct\n"
        #                 .format(guess)).casefold()

        # if high_low == "h":
        if guess < answer:
            # Guess higher. The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l":
        elif guess > answer:
            # Guess lower. The high end of the range becomes one less than the guess.
            high = guess - 1
        # elif guess == "c":
        elif guess == answer:
            # print("I got it in {} guesses!".format(guesses))
            # break
            return guesses

        guesses += 1


correct_count = 0
max_guesses = 0
for number in range(LOW, (HIGH + 1) - 0):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("I guessed without being told {} times. Max {} guesses."
      .format(correct_count, max_guesses))

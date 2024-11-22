def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    separators = " ,.'"
    string = "".join(char if char not in separators else "" for char in sentence).split()
    string = str(string[0])
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


# answer = multiply(10.5, 4)
# print(answer)
# answer = multiply(10, 5)
# print(answer)
# for val in range(1, 5):
#     two_times = multiply(val, 2)
#     print(two_times)

# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not palindrome".format(word))

# input_sentence = input("Please enter a palindrome sentence: ")
# if palindrome_sentence(input_sentence):
#     print("\'{}\' is a palindrome".format(input_sentence))
# else:
#     print("\'{}\' is not palindrome".format(input_sentence))

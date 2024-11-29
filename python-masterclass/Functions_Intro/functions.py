def multiply(x: float, y: float) -> float:
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    separators = " ,.'"
    string = "".join(char if char not in separators else "" for char in sentence).split()
    string = str(string[0])
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    n = int(n)

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


# --- Multiply test ---
# answer = multiply(10.5, 4)
# print(answer)
# answer = multiply(10, 5)
# print(answer)
# for val in range(1, 5):
#     two_times = multiply(val, 2)
#     print(two_times)

# --- Palindrome test ---
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

fib = fibonacci(15)
print(fib)
fib = fibonacci(0)
print(fib)
fib = fibonacci(-1)
print(fib)

for i in range(36):
    print(i, fibonacci(i))

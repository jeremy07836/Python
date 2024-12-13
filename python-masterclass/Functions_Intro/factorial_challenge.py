def factorial(n: int) -> int:
    """
    Returns the factorial of `n` number
    :param n: integer
    :return: factorial of `n`
    """
    total = 1
    if n == 0 or n == 1:
        return total

    for number in range(1, n + 1):
        total = total * number

    return total


for n_test in range(0, 11):
    t = factorial(n_test)
    print("{} {}".format(n_test, t))

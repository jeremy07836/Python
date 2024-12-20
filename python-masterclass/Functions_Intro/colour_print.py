import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'
# print(RED, "this will be in red")
# print("and so is this")
# input("Press enter to end:")


def colour_print(text: str, *effects: str) -> None:
    """
    Print `text` using ANSI sequences to change text's colour, etc

    :param text: The text to print
    :param effects: The ANSI sequences to effect the text
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


colorama.init()
colour_print("Hello, Red", RED)
colour_print("Hello, Red", RED, BOLD)
print("Default terminal colour")
colour_print("Blue", BLUE)
colour_print("Blue", BLUE, REVERSE)
colour_print("Blue", BLUE, REVERSE, UNDERLINE)
colour_print("Yellow", YELLOW)
colour_print("Yellow", YELLOW, BOLD)
colour_print("Bold", BOLD)
colour_print("Underlined", UNDERLINE)
colour_print("Reversed", REVERSE, UNDERLINE)
colour_print("Black", BLACK)
colorama.deinit()

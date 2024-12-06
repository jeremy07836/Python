def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Prints the text centered with two * characters at the beginning and end

    :param text: The text that is printed; throws an error if longer than width - 4
    :param screen_width: The specified width of the string
    :raise ValueError: if the length is too long
    """
    if len(text) > screen_width - 4:
        raise ValueError("String: {0}\nis larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


width = 60
banner_text()
try:
    banner_text("*", width)
    banner_text("Always look on the bright side of life...", width)
    banner_text("If life seems jolly rotten,", width)
    banner_text("There's something you've forgotten!", width)
    banner_text("And that's to laugh and smile and dance and sing,", width)
    banner_text(screen_width=width)
    banner_text("When you're feeling in the dumps,", width)
    banner_text("Don't be silly chumps,", width)
    banner_text("Just purse your lips and whistle - that's the thing!", width)
    banner_text("And... always look on the bright side of life...", width)
    banner_text("*", width)
except ValueError as e:
    print(e)

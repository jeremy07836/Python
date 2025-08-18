def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    text = text.rstrip(sep)
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open("centred", mode='w') as centred:
# call the function
# s1 = centre_text("spam and eggs")
# print(s1)
# s2 = centre_text("spam, spam and eggs")
# print(s2)
# s3 = centre_text(12)
# print(s3)
# s4 = centre_text("spam, spam, spam and spam")
# print(s4)
# s5 = centre_text(python_food())
# print(s5)
# s6 = centre_text("first", "second", 3, 4, "spam", sep=':')
# print(s6)

with open("menu", "w") as menu:
    s1 = centre_text("spam and eggs")
    print(s1, file=menu)
    s2 = centre_text("spam, spam and eggs")
    print(s2, file=menu)
    s3 = centre_text(12)
    print(s3, file=menu)
    s4 = centre_text("spam, spam, spam and spam")
    print(s4, file=menu)
    s5 = centre_text(python_food())
    print(s5, file=menu)
    s6 = centre_text("first", "second", 3, 4, "spam", sep=':')
    print(s6, file=menu)

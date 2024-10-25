menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

for meal in menu:
    #print("[", end="")
    # for item in meal:
    #     if item != "spam":
    #         print("'{}'".format(item), end=", ")
    # print("]", end="")
    # print()
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)

print("*" * 80)

for meal in menu:
    top_index = len(meal) - 1
    for index, value in enumerate(reversed(meal)):
        if value == "spam":
            del meal[top_index - index]
    print(", ".join(meal))

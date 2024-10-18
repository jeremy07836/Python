available_part = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mousepad",
                  "hdmi",
                  "dvd drive"
                  ]
valid_choices = [str(i) for i in range(1, len(available_part) + 1)]
# valid_choices = []
# for i in range(1, len(available_part) + 1):
#     valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []  # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_part[index]
        if chosen_part in computer_parts:
            print("Removed part {}".format(chosen_part))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_part):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()
else:
    print(computer_parts)
    print("Ending program")

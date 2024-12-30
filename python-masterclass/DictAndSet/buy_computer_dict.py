available_part = {"1": "computer",
                  "2": "monitor",
                  "3": "keyboard",
                  "4": "mouse",
                  "5": "mousepad",
                  "6": "hdmi",
                  "7": "dvd drive"
                  }

current_choice = None
computer_parts = {}     # create an empty dictionary

while current_choice != "0":
    if current_choice in available_part:
        chosen_part = available_part[current_choice]
        if current_choice in computer_parts:
            # already in
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains {computer_parts}")
    else:
        print("Enter the number to add item to cart")
        for key, value in available_part.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")

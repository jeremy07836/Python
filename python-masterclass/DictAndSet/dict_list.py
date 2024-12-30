available_part = {"1": "computer",
                  "2": "monitor",
                  "3": "keyboard",
                  "4": "mouse",
                  "5": "mousepad",
                  "6": "hdmi",
                  "7": "dvd drive"
                  }
computer_parts = []

current_choice = None
while current_choice != "0":
    if current_choice in available_part:
        chosen_part = available_part[current_choice]
        if chosen_part in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
    else:
        print("Enter the number to add item to cart")
        for key, value in available_part.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")

print(computer_parts)

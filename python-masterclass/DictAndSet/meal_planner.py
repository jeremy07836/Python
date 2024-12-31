from contents import pantry, recipes

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
for index, key in enumerate(recipes):
    # print(index + 1, key)
    display_dict[str(index + 1)] = key

print(display_dict)
while True:
    # Display a menu of recipes
    print("Please choose a recipe")
    print("-" * 20)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        # print(f"Ingredients include: {ingredients}")

        # this fails because of error,
        #   can not check if a list is in a dict
        #   enumerate(pantry) does not work
        #   pantry.items does not work
        #
        # if ingredients in pantry:
        #     print(pantry)
        #     print("All ingredients are in the pantry")

        for item in ingredients:
            if item in pantry:
                print(f"{item} OK")
            else:
                print(f"{item} not found")
        # break
    else:
        print("\nInvalid choice, enter a number for the recipe")

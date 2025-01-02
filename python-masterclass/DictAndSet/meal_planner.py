from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tuple to containing `item` and `amount` to the `data` dict."""
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount


# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
shopping_cart = {}
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
        print(f"Ingredients include: {ingredients}")

        # this fails because of error,
        #   can not check if a list is in a dict
        #   enumerate(pantry) does not work
        #   pantry.items does not work
        #
        # if ingredients in pantry:
        #     print(pantry)
        #     print("All ingredients are in the pantry")

        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"{food_item} OK")
                # does not update dictionary
                # pantry[item] = {item: (quantity_in_pantry - required_quantity)}
                # print(f"Update {item} in pantry -> {pantry[item]}")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} {food_item}")
                # shopping_cart.append((item, quantity_to_buy))
                add_shopping_item(shopping_cart, food_item, quantity_to_buy)
                # print(f"Shopping cart:\n{shopping_cart}")
        # break
    else:
        print("\nInvalid choice, enter a number for the recipe")

print("\nShopping Cart:")
print("-" * 20)
for item, quantity in shopping_cart.items():
    print(f"{item} - {quantity}")

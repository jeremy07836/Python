menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#         # print(meal)
#     else:
#         meals.append("a meal was skipped")
# print(meals)
#
# # meals = [meal for meal in menu if "spam" not in meal]
# meals = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
# print(meals)
#
# x = 12
# # x = 15
# expression = "Twelve" if x == 12 else "unknown"
# print(expression)

for meal in menu:
    # print(meal, "contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains egg")
    print(meal, "contains sausage" if "sausage" in meal else "contains bacon" if "bacon" in meal else "contains egg")

print()

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)
print()

for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break

for x in range(1, 31):
    x15 = x % 15 == 0
    x3 = x % 3 == 0
    x5 = x % 5 == 0
    fizzbuzz = "fizz buzz" if x15 else "fizz" if x3 else "buzz" if x5 else str(x)
    print(fizzbuzz)

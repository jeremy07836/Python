# numbers = {}
# numbers = {*""}
numbers = set()

# numbers.add(1)
# print(numbers, type(numbers))

# while len(numbers) < 4:
#     next_value = int(input("Please enter you next value: "))
#     numbers.add(next_value)
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list, to remove duplicates
unique_data = sorted(set(data))
print(unique_data)

# Create a list of unique colors, keeping the order the appeared
unique_data = list(dict.fromkeys(data))
print(unique_data)

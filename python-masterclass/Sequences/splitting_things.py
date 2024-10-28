panagram = """The quick brown 
fox jumps\tover
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

# separators = ",.-_"
# values1 = "".join(char if char not in separators else " " for char in numbers).split()
# print(values1)

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

# for index, val in enumerate(values_list):
#     values_list[index] = int(val)
#
# print(values_list)

values_numbers = []
for val in values_list:
    values_numbers.append(int(val))

print(values_numbers)

# print("Please enter some numbers: ")
input_value = input()

numbers = "".join(input_value)
# print(numbers)
numbers = numbers.split(",")
# print(numbers)

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

total_value = a + b - c
print(total_value)

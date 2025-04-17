data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename = "flowers_print.txt"
# with open(plants_filename, "w") as plants:
#     print(f"Write data to file: {plants_filename}")
#     print(f"\t{data}")
#     for plant in data:
#         print(plant, file=plants)
#     print("Finished print to file\n")
#
# new_lists = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_lists.append(plant.rstrip())
#
# print(new_lists)

# plants_filename = "flowers_write.txt"
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         plants.write(plant)
#
# print(data)
# string_rep = data.__str__()
# print(type(string_rep))

filename = "test_numbers.txt"
with open(filename, "w") as test:
    for i in range(10):
        print(i, file=test)

# Fails if not using string
with open(filename, "w") as test:
    for i in range(10):
        test.write(str(i) + "\n")

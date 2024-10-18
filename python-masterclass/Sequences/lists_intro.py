computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# computer_parts[3] = "trackball"
print(computer_parts[3:])
computer_parts[3:] = ["trackball"]
print(computer_parts)


# for part in computer_parts:
#     print(part)
#
# print()
# print(computer_parts[2])

# data = [
#     "Andromeda - Shrub",
#     "Bellflower - Flower",
#     "China Pink - Flower",
#     "Daffodil - Flower",
#     "Evening Primrose - Flower",
#     "French Marigold - Flower",
#     "Hydrangea - Shrub",
#     "Iris - Flower",
#     "Japanese Camellia - Shrub",
#     "Lavender - Shrub",
#     "Lilac - Shrub",
#     "Magnolia - Shrub",
#     "Peony - Shrub",
#     "Queen Anne's Lace - Flower",
#     "Red Hot Poker - Flower",
#     "Snapdragon - Flower",
#     "Sunflower - Flower",
#     "Tiger Lily - Flower",
#     "Witch Hazel - Shrub",
# ]
#
# flowers = []
# shrubs = []
#
# # write your code here
#
# for d in data:
#     d_strings = d.split(" - ")
#     d_name = d_strings[0]
#     d_type = d_strings[1]
#     if "Flower" in d_type:
#         flowers.append(d_name)
#     if "Shrub" in d_type:
#         shrubs.append(d_name)
#
# print(flowers)
# print(shrubs)

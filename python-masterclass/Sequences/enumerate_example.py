# for index, character in enumerate("abcdefgh"):
#     print(index, character)

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character, sep=", ")

index, character = (0, 'a')
print(index, character, sep=", ")

from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

apple_quantity = pantry.setdefault("apple", 0)
print(f"apples: {apple_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")

a_quantity = pantry.setdefault("almonds", 0)
print(f"almonds: {a_quantity}")

print()
print("`pantry` now contains...")
for key, value in sorted(pantry.items()):
    print(key, value)

# Challenge
# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
for text_letter in text:
    letter_lower = text_letter.casefold()
    other_letters = " ',."
    if letter_lower not in other_letters:
        word_count[letter_lower] = word_count.setdefault(letter_lower, 0) + 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)

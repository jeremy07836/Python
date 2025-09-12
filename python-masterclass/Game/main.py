from player import Player

jeremy = Player("Jeremy")

print(jeremy.name)

print(jeremy)
jeremy.lives -= 1

print(jeremy)
jeremy.lives -= 1

print(jeremy)
jeremy.lives -= 1

print(jeremy.lives)
jeremy.lives = -11
print(jeremy.lives)
jeremy.lives -= 11
print(jeremy.lives)

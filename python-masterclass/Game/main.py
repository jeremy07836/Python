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

jeremy.level = 5
print(jeremy.name, jeremy.level, jeremy.score)

jeremy.level -= 3
print(jeremy.name, jeremy.level, jeremy.score)

jeremy.level -= 5
print(jeremy.name, jeremy.level, jeremy.score)

jeremy.score = 500
print(jeremy.score)

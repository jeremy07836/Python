from player import Player
from enemy import Enemy, Troll

jeremy = Player("Jeremy")

troll1 = Troll()
print(troll1)

troll2 = Troll("Ug", 18, 1)
print("Another troll - {}".format(troll2))

troll3 = Troll("Urg", 23)
print(troll3)

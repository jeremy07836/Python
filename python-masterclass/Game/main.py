from player import Player
from enemy import Enemy, Troll, Vampyre

jeremy = Player("Jeremy")

ugly_troll = Troll("Pug")
ugly_troll.take_damage(5)
ugly_troll.take_damage(50)
ugly_troll.take_damage(50)
print(ugly_troll)

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vamp1 = Vampyre("Vlad")
vamp1.take_damage(13)
vamp2 = Vampyre("Tom")
print(vamp1)
print(vamp2)

while vamp1.alive:
    vamp1.take_damage(1)
    print(vamp1)

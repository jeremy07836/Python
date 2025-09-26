from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

jeremy = Player("Jeremy")

vamp_king = VampyreKing("Dracula")
vamp_king.take_damage(5)
vamp_king.take_damage(4)
vamp_king.take_damage(3)
vamp_king.take_damage(3)
vamp_king.take_damage(20)
print(vamp_king)

# ugly_troll = Troll("Pug")
# ugly_troll.take_damage(5)
# ugly_troll.take_damage(50)
# ugly_troll.take_damage(50)
# print(ugly_troll)
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# vamp1 = Vampyre("Vlad")
# vamp1.take_damage(13)
# vamp2 = Vampyre("Tom")
# print(vamp1)
# print(vamp2)

# while vamp1.alive:
#     vamp1.take_damage(1)
#     print(vamp1)

# vamp1._lives = 0
# vamp1._hit_points = 1
# print(vamp1)

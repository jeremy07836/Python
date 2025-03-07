# farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
# wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
#
# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)
#
# all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)
#
# all_animals_3 = wild_animals | farm_animals
# print(all_animals_3)

from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
#     # new set
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch = meds_to_watch | interaction
#
#     # update set
#     # meds_to_watch.update(interaction)
#     meds_to_watch |= interaction

meds_to_watch.update(*adverse_interactions)

print(adverse_interactions)
print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')

scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellow-jacket", "hornet", "paper wasp"}

bite = set()
bite.update(snakes, spiders)
print('Things that bite:', sorted(bite))

sting = set()
sting |= scorpions | vespas
print('Things that sting:', sorted(sting))

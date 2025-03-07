# trial_1 = {"Bob", "Charley", "Georgia", "John"}
# trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}
#
# check_set = trial_1.intersection(trial_2)
# print(check_set)

farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
wild_animals = {'lion', 'elephant', 'tiger', 'goats', 'panther', 'horse'}
potential_rides = {'donkey', 'horse', 'camel'}

intersect = farm_animals & wild_animals & potential_rides
print(intersect)

mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)

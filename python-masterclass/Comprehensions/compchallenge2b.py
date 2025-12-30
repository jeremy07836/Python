# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that lead to each of the
# other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.


locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

print("nested for loops")
print("-" * 20)
for loc in sorted(locations):
    exits_to_dest_1 = []
    for ex in exits:
        if loc in exits[ex].values():
            exits_to_dest_1.append((ex, locations[ex]))
    print("Locations leading to {}". format(loc), end='\t')
    print(exits_to_dest_1)
print()
print("List comprehension inside a for loop")
print("-" * 40)

for loc in sorted(locations):
    exit_to_dest_2 = [(ex, locations[ex]) for ex in exits if loc in exits[ex].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(exit_to_dest_2)
print()

print("nested comprehension")
print("-" * 30)
exits_to_dest_3 = [[(ex, locations[ex]) for ex in exits if loc in exits[ex].values()]
                   for loc in sorted(locations)]
print(exits_to_dest_3)
print()
for index, loc in enumerate(exits_to_dest_3):
    print("Locations leading to {}".format(loc), end='\t')
    print(loc)

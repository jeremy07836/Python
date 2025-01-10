from simple_deepcopy import copy_dict
import copy

original = {
    "Jeremy": ["Nearing", ["QA", "Gamer"]],
    "testing": ["lastname", ["1", "2"]]
}

copy_1 = copy.deepcopy(original)
copy_2 = copy_dict(original)

original["Jeremy"].append("Canada")
original["testing"].append("USA")

original["Jeremy"][1].append("Grocery")
test_list = original["testing"]
test_list[1].append("Courier")

print(id(original), original)
print(id(copy_1), copy_1)
print(id(copy_2), copy_2)
print(id(test_list), test_list)

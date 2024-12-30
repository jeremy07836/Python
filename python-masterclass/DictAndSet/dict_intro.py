vehicles = {
    'dream': 'Honda 250T',
    #'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triump Street Triple',
}

for key, value in vehicles.items():
    print(key, value, sep=' - ')

# my_car = vehicles['fiesta']
# print(my_car)
# Crashes
# my_car = vehicles['Fiesta']
# print(my_car)
# learner = vehicles.get("er5")
# print(learner)
# Errors out
# learner = vehicles.get("ER5")
# print(learner)

# for key in vehicles:
#     print(key, vehicles[key], sep=' - ')

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# Upgrade the Virago
vehicles["virago"] = "Yamaha XV535"


del vehicles["starfighter"]
# fails
# del vehicles["f1"]
result = vehicles.pop("f1", "You wish! Sell teh Learjet and you might afford it.")
print("\n", result, sep="")

plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)

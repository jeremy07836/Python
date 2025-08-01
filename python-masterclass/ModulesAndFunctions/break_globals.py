import better_code
from better_code import area_of_square

area = better_code.area_of_square(40)
area2 = area_of_square(40)

print(area)
print(area2)
print('Global namespace')
namespace = globals()   # .copy()
for name, obj in namespace.items():
    print(name, obj)

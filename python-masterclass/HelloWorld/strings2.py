#
#         0123456789
parrot = "Norwegian Blue"

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

letters = "abcdefghijklnmopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards)

backwards = letters[::-1]
print(backwards)

'''
print(parrot[-14:-8])
print(parrot[-4:-2])
print(parrot[-4:12])


print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])
print(parrot[:])


print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
'''

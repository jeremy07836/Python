print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
#name = input("Please enter your name: ")
name = 'jeremy'
# if we want a space
print(greeting + ' ' + name)

age = 31
print(age)

print(type(greeting))
print(type(age))

age_in_words = "31 years"
print(type(age_in_words))
# type error
# print(name + " is " + age + " years old")
print(name + f" is {age} years old")

print(f"Pi is approximately {22/7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

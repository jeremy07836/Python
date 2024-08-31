string1 = "he's "
string2 = "probably "
string3 = "for the "
string4 = "fjords"

print(string1 + string2 + string3 + string4)
print("he's " "probably " "for the " "fjords")
print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today)       # true
print("fri" in today)       # true
print("thur" in today)      # false
print("parrot" in "fjord")  # false

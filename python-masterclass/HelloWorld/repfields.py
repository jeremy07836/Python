age = 31
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, June: {1}, July: {2}, Sept: {1}, Oct: {2}"
      .format(28, 30, 31))

print("""
Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
June: {1}
July: {2}
Sept: {1}
Oct: {2}
""".format(28, 30, 31))

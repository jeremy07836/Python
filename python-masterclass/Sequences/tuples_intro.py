# t = ("a", "b", "c")
# print(t, t[0])
#
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# metallica[0] = "Master of Puppets"   # This fails and causes an error
#
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# metallica2 = list(metallica)
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# metallica2[2] = 1986
# # print(metallica2)
#
# title, artist, year = metallica
# print(title, artist, year, sep=", ")

table = ("Coffee table", 200, 100, 75, 34.50)
name, length, width, height, price = table
print(length * width)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975,
           (
               (1, "Song1")
           )),
          ("Bad Company", "Bad Company", 1974,
           (
               (1, "Song1")
           )),
          ("Nightflight", "Budgie", 1981,
           (
               (1, "Song1")
           )),
          ("More Mayhem", "Emilda May", 2011,
           (
               (1, "Song1")
           )),
          ("Ride the Lightning", "Metallica", 1984,
           (
               (1, "Song1")
           )),
          ]

print(len(albums))
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Moving On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# for index, value in enumerate(albums):
#     title, artist, year, songs = value
#     print("{}: {}".format(index, value))
#     print(title, artist, year, songs)

print("Choose your album:")
for index, (name, artist, year, songs) in enumerate(albums):
    print("{}: {}"
          .format(index + 1, name))

album_number = int(input())
if album_number <= len(albums):
    print(len(albums))
    album_number -= 1

    print("Choose your song:")
    for index, song in enumerate(albums[album_number][3]):
        print("{}: {}".format(index + 1, song))

    album_song = int(input())
    if album_number <= len(albums[album_number][3]):
        album_song -= 1
        print(albums[album_number][3][album_song][1])
    else:
        print("Number is incorrect")
else:
    print("Number is incorrect")

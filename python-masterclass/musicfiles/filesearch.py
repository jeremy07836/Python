import os
import fnmatch

def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directories, artist_name):
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            # print(artist)
            subdir = str(os.path.join(path, artist))
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):   # we want the path, not the name of the album
            yield song


def get_song_path(albums):
    for path in albums:
        album_dir = path[0]
        for _, _, songs in os.walk(album_dir):
            for song in songs:
                # print(path, song)
                fullpath = album_dir + '\\\\' + song
                yield fullpath

album_list = find_albums("music", "Black*")

song_list = find_songs(album_list)

songs = get_song_path(album_list)
for song_path in songs:
    print(song_path)

# for a in album_list:
#     print(a)

for s in song_list:
    # print(s)
    pass

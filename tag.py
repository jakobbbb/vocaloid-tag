import eyed3
from song import Song


def tag_song(path, song: Song):
    print(path)
    print(song)

    audiofile = eyed3.load(path)
    audiofile.tag.artist = song.artist
    audiofile.tag.title = song.title
    if song.year is not None:
        audiofile.tag.year = song.year
    audiofile.tag.save()

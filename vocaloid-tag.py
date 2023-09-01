#!/usr/bin/env python3
from vocadb import VocaDB
from song import Song
from tag import tag_song
from song import SongNotFoundError
import re
from os import listdir, path
from shutil import copy
from sys import argv

YT_DLP_EXP = re.compile(r".*\[(?P<yt_id>[a-zA-Z0-9-_]{11})\].*.mp3")


def get_yt_id(filename: str):
    if m := YT_DLP_EXP.match(filename):
        return m.group("yt_id")
    return None


def tag_yt_song(song_path: str, lang: str) -> Song:
    yt_id = get_yt_id(song_path)
    if not yt_id:
        raise SongNotFoundError()
    song = VocaDB.search_by_yt_id(yt_id, lang)
    tag_song(song_path, song)
    return song


def nice_filename(song: Song) -> str:
    return f"{song.artist} - {song.title}.mp3"


def tag_dir(song_dir: str, target_dir: str, lang: str):
    for f in listdir(song_dir):
        if f.endswith(".mp3"):
            song_path = path.join(song_dir, f)
            try:
                song = tag_yt_song(song_path, lang)
                copy(song_path, path.join(target_dir, nice_filename(song)))
            except SongNotFoundError as e:
                print(f"Could not find song for {f}: '{e}'")
            except Exception as e:
                print(f"An unexpected error occured finding data for {f}:")
                print(e)


def main():
    if len(argv) >= 3:
        tag_dir(
            song_dir=argv[1],
            target_dir=argv[2],
            lang=argv[3] if len(argv) >= 4 else "Default",
        )
    else:
        print(
            f"usage: ./{argv[0]} <directory with downloaded mp3s> "
            "<target dir> [optional: language (Default, Japanese, Romaji, English)]"
        )


if __name__ == "__main__":
    main()

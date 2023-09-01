# vocaloid-tag

Tool for tagging and renaming Vocaloid songs downloaded from YouTube.

## usage

```
./vocaloid-tag.py <directory with downloaded mp3s> <target dir> [language (Default, Japanese, Romaji, English)]
```

### full example
```sh
yt-dlp -x -f bestaudio https://www.youtube.com/watch\?v\=uKbRXeJ9lv4
mkdir mp3
for f in *opus; do ffmpeg -i $f -ab 320k mp3/$f.mp3; done
/path/to/vocaloid-tag/vocaloid-tag.py ./mp3 /path/to/destination
```

The output filename will be: `きくお - イイコと妖狐.mp3`

### language

You can specify the langauge like this:

```
# Kikuo - The Good Child and the Fox Spirit.mp3
/path/to/vocaloid-tag/vocaloid-tag.py ./mp3 /path/to/destination English

# Kikuo - Ii Ko to Youko.mp3
/path/to/vocaloid-tag/vocaloid-tag.py ./mp3 /path/to/destination Romaji

# きくお - イイコと妖狐.mp3
/path/to/vocaloid-tag/vocaloid-tag.py ./mp3 /path/to/destination Romaji
```

By default, it uses whatever vocadb defaults to.

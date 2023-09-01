# vocaloid-tag

Tool for tagging and renaming Vocaloid songs downloaded from YouTube.

## usage

```sh
yt-dlp -x -f bestaudio https://www.youtube.com/watch\?v\=uKbRXeJ9lv4
mkdir mp3
for f in *opus; do ffmpeg -i $f -codec:a libmp3lame -b:v 320 mp3/$f.mp3; done
/path/to/vocaloid-tag/vocaloid-tag.py ./mp3 /path/to/destination
```

The output filename will be: `きくお feat. 绮萱 - イイコと妖狐.mp3`

You can specify the langauge like this:

```
# Kikuo feat. Qǐxuān - The Good Child and the Fox Spirit.mp3
/path/to/vocaloid-tag/vocaloid-tag.py ./mp3 /path/to/destination English

# Kikuo feat. Qǐxuān - Ii Ko to Youko.mp3
/path/to/vocaloid-tag/vocaloid-tag.py ./mp3 /path/to/destination Romaji

# きくお feat. 绮萱 - イイコと妖狐.mp3
/path/to/vocaloid-tag/vocaloid-tag.py ./mp3 /path/to/destination Romaji
```

By default, we'll use whatever vocadb defaults to.

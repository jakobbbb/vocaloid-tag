from song import Song, SongNotFoundError
import requests
from urllib.parse import urljoin


class VocaDB:
    @staticmethod
    def __query(endpoint, params):
        headers = {"User-Agent": "vocaloid-tag (contact: github.com/jakobbbb)"}
        base = "https://vocadb.net/api/"
        url = urljoin(base, endpoint)
        return requests.get(url, params=params, headers=headers)

    @staticmethod
    def search_by_yt_id(yt_id: str, lang="Default") -> Song:
        if len(yt_id) != 11:
            raise SongNotFoundError()

        endpoint = "songs/byPv"
        params = {
            "pvService": "Youtube",
            "pvId": yt_id,
            "lang": lang,
        }

        resp = VocaDB.__query(endpoint, params)
        data = resp.json()
        print(resp.url)

        if resp.status_code != 200 or data is None:
            raise SongNotFoundError("Song not found.")

        return Song(
            artist=data["artistString"],
            title=data["name"],
            year=int(data["publishDate"][:4]) if data["publishDate"] else None,
        )

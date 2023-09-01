from typing import Union
from dataclasses import dataclass


@dataclass
class Song:
    title: str
    artist: str
    year: Union[int, None]


class SongNotFoundError(RuntimeError):
    pass

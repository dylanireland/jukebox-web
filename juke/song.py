from web3 import Web3
import json

class Song:
    def __init__(self, url, coverUrl, title, artist, publisher, start, end):
        self.url = url
        self.coverUrl = coverUrl
        self.title = title
        self.artist = artist
        self.publisher = publisher
        self.start = start
        self.end = end

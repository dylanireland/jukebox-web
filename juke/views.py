from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from web3 import Web3
from .song import Song
import json
from .contract import Contract

# Create your views here.

def index(request):
    infuraUrl = Contract.getinfUrl()
    web3 = Web3(Web3.HTTPProvider(infuraUrl))

    abi = json.loads(Contract.getAbi())
    address = web3.toChecksumAddress(Contract.getAddy())

    contract = web3.eth.contract(address=address, abi=abi)

    try:
        qLength = contract.functions.getQueueLength().call()
    except:
        return HttpResponse("Something went wrong 100")

    queueDepth = getQueueDepth(contract)
    if queueDepth is None:
        return HttpResponse("Something went wrong 101")

    queue = getQueue(contract, queueDepth, qLength)
    if queue == None:
        return HttpResponse("Something went wrong 102")

    try:
        _, _, _, _, songPublisher, _, _ = contract.functions.getCurrentSong().call()
        if songPublisher == "0x0000000000000000000000000000000000000000":
            raise
    except:
        queue = []

    queue = queue[:15]

    template = loader.get_template('juke/index.html')
    context = {"queue": [trunc(song) for song in queue], "faq": getFAQ()}
    return HttpResponse(template.render(context, request))


def getQueueDepth(contract):
    try:
        return contract.functions.getQueueDepth().call()
    except:
        return None

def getQueue(contract, queueDepth, queueLength):
    dict = []
    for i in range(queueDepth):
        try:
            songUrl, songCoverUrl, songTitle, songArtist, songPublisher, start, end = contract.functions.getSongAtIndex(queueLength - i - 1).call()
            song = Song(songUrl, songCoverUrl, songTitle, songArtist, songPublisher, start, end)
            dict.append(song)
        except:
            return None
    newDict = []
    while queueDepth > 0:
        newDict.append(dict[queueDepth - 1])
        queueDepth = queueDepth - 1
    return newDict

def getFAQ():
    dict = {
        "How do I listen to Jukebox?": "To listen, simply visit the <a href='app' class='colorfulLink'>Jukebox dApp</a> and press play! Once you've done so, the queue will continue to play until you pause it or close the tab.",
        "How do I add a song to Jukebox?": "To add a song to the Jukebox queue, visit the <a href='app' class='colorfulLink'>Jukebox dApp</a> and select \"Add Song\". You may provide a direct link to an audio file or a download link for an audio file. You may also input a YouTube video link to be converted to audio.",
        "Are there fees to use Jukebox?": "There are no fees for listening to music; it is free and always will be. Adding songs to the queue does however include fees paid in Ether and is more expensive the longer the queue and the longer the song. See <a href='economics' class='colorfulLink'>Fee Pricing</a>",
        "What happens to fees paid by song publishers?": "Fees paid in Ether are stored in a smart contract and will be used to swap for JUK tokens when v2 is released. See <a href='future-work' class='colorfulLink'>Future Work</a>",
        "Can I choose when my song plays?": "At this time, songs are added to the queue sequentially and it is not possible to select a block interval to have your song play. This may change in the future.",
        "Can I sell my time slot back to Jukebox?": "Currently, once you purchase the right to have your song played, it will play during the designated interval and that cannot be changed or refunded. In v2, time slots will be able to be sold as NFTs. See <a href='future-work' class='colorfulLink'>Future Work</a>"
        }
    return dict.items()

def trunc(song):
    if len(song.title) > 35:
        song.title = song.title[:35] + "..."

    if len(song.artist) > 30:
        song.artist = song.artist[:30] + "..."

    return song

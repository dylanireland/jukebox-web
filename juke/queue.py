from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .contract import Contract
from .song import Song
from web3 import Web3
import json

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

    template = loader.get_template('juke/queue.html')
    context = {"queue": [trunc(song) for song in queue]}
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

def trunc(song):
    if len(song.title) > 35:
        song.title = song.title[:35] + "..."

    if len(song.artist) > 30:
        song.artist = song.artist[:30] + "..."

    return song

from web3 import Web3
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import json
from .song import Song
from urllib.request import urlopen, Request
from django.conf import settings
import os
from .forms import AddSongForm
from .models import TaskLogger
from .contract import Contract


# Create your views here.

def index(request):
    template = loader.get_template('juke/app.html')

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

    context = {"queue": queue[1:10], "form": AddSongForm(), "addy": Contract.getAddy(), "blockNumber": web3.eth.blockNumber}

    try:
        songUrl, songCoverUrl, songTitle, songArtist, songPublisher, start, end = contract.functions.getCurrentSong().call()
        if songPublisher == "0x0000000000000000000000000000000000000000":
            raise
    except:
        context['song'] = Song("","","Queue Empty","","",0,0)
        return HttpResponse(template.render(context, request))

    localSongName = str(start) + '.mp3'

    currentSong = Song('songs/' + str(start) + '.mp3', songCoverUrl, songTitle, songArtist, songPublisher, start, end)
    context['song'] = currentSong

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

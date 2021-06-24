from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from web3 import Web3
from .song import Song
import json
from .contract import Contract
import boto3

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


    template = loader.get_template('juke/index.html')
    context = {"queue": queue[:15], "faq": getFAQ()}
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

        "How do I add a song to Jukebox?": "To add a song to the Jukebox queue, visit the <a href='app' class='colorfulLink'>Jukebox dApp</a> and select \"Add Song\". You may provide a direct link to an audio file or a download link for an audio file. You may also input a YouTube video link to be converted to audio.",
        "Are there fees to use Jukebox?": "There are no fees for listening to music; it is free and always will be. Adding songs to the queue does however include fees calculated in USD and paid in Ether and is more expensive the longer the queue and the longer the song. See <a href='tokenomics' class='colorfulLink'>Fee Pricing</a>",
        "How are fees distributed?": "Fees paid in Ether are stored in a smart contract and will be used to swap for JUK tokens when v2 is released.",
        "What are JUK tokens?": "JUK tokens will be ERC20 tokens that will be used to pay Jukebox fees. In v2, all fees must be paid with JUK tokens and <b>ALL</b> fee payments will be burned. See <a href='tokenomics' class='colorfulLink'>Tokenomics</a>",
        "Where can I get JUK tokens?": "JUK tokens do not yet exist but the best way to acquire them is to publish songs to Jukebox. Upon release of v2 all previous users will receive an airdrop of JUK tokens. Those who added more songs will receive higher tiers."
        }
    return dict.items()

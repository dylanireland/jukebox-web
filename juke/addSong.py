from __future__ import unicode_literals
from web3 import Web3
from web3.middleware import geth_poa_middleware
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
import json
from .song import Song
from urllib.request import urlopen, Request
from django.conf import settings
import os
import youtube_dl
from .forms import AddSongForm
from .contract import Contract

# Create your views here.

def index(request):
    if request.method != 'POST':
        return HttpResponseFordbidden("You are not authorized")

    infuraUrl = Contract.getinfUrl()
    web3 = Web3(Web3.HTTPProvider(infuraUrl))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    abi = json.loads(Contract.getAbi())
    address = web3.toChecksumAddress(Contract.getAddy())

    contract = web3.eth.contract(address=address, abi=abi)
    account = web3.eth.coinbase
    nonce = web3.eth.get_transaction_count(account)




    url = request.POST.get('url')
    coverUrl = request.POST.get('coverUrl')
    title = request.POST.get('title')
    artist = request.POST.get('artist')
    duration = int(request.POST.get('duration'))

    if url == None or coverUrl == None or title == None or artist == None or duration == None or url == "" or coverUrl == "" or title == "" or artist == "" or duration <= 0:
        return HttpResponseBadRequest("Bad data")

    txn = contract.functions.addSong(url, coverUrl, title, artist, duration).buildTransaction({'chainId': 4, 'gas': 131000, 'gasPrice': web3.toWei('1', 'gwei'), 'nonce': nonce })
    signed_tx = web3.eth.account.sign_transaction(tx, key)
    web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    #songAddedHash = contract.functions.addSong(url, coverUrl, title, artist, duration).transact()
    #blockNumber = web3.eth.wait_for_transaction_receipt(songAddedHash)["blockNumber"]
    try:
        startTime = contract.functions.getNextStartTime().call()
    except:
        return HttpResponse("Done but song not saved")

    saveFromYoutube(url, startTime if startTime != 0 else web3.eth.blockNumber)




    return HttpResponse(startTime)

def saveFromYoutube(url, blockNumber):
    ydl_opts = {'format': 'bestaudio/best', 'extractaudio': True, 'audioformat': 'mp3', 'outtmpl': 'juke/static/songs/' + str(blockNumber) + '.mp3', 'noplaylist': True, 'nocheckcertificate':True, 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': '192'}],}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

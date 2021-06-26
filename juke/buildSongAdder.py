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
from .forms import AddSongForm
from .contract import Contract
from eth_abi import encode_abi

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


    url = request.POST.get('url')
    coverUrl = request.POST.get('coverUrl')
    title = request.POST.get('title')
    artist = request.POST.get('artist')
    duration = int(request.POST.get('duration'))

    if duration > 255:
        return HttpResponseBadRequest("Duration may not be longer than 255 blocks.")

    if url == None or coverUrl == None or title == None or artist == None or duration == None or url == "" or coverUrl == "" or title == "" or artist == "" or duration <= 0:
        return HttpResponseBadRequest("Bad data")


    data = contract.encodeABI(fn_name="addSong", args=[url, coverUrl, title, artist, duration])

    gasLimit = contract.functions.addSong(url, coverUrl, title, artist, duration).estimateGas() + 30000

    return HttpResponse(data + "%" + str(hex(gasLimit)))

    #return (HttpResponse(contract.encodeABI(fn_name="addSong", args=[url, coverUrl, title, artist, duration])), HttpResponse(contract.functions.addSong(url, coverUrl, title, artist, duration).estimateGas()))

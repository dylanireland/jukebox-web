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

    if url == None or coverUrl == None or title == None or artist == None or duration == None or url == "" or coverUrl == "" or title == "" or artist == "" or duration <= 0:
        return HttpResponseBadRequest("Bad data")

    return HttpResponse(contract.encodeABI(fn_name="addSong", args=[url, coverUrl, title, artist, duration]))

    #return HttpResponse(encode_abi(['string', 'string', 'string', 'string', 'uint256'], [url, coverUrl, title, artist, duration]))

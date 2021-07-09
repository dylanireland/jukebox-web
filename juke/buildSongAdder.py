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
import boto3
import uuid

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
    value = int(request.POST.get('value'))
    file = request.FILES.get('song')
    covfile = request.FILES.get('covfile')

    if duration > 255:
        response = HttpResponse("Duration may not be longer than 255 blocks.")
        response.status_code = 400
        return reponse

    if title is None or artist is None or duration is None or title == "" or artist == "" or duration <= 0  or (covfile is None and (coverUrl == "" or coverUrl is None)) or (((not coverUrl is None) and coverUrl != "") and not covfile is None) or (file is None and (url == "" or url is None)) or (((not url is None) and url != "") and not file is None):
        response = HttpResponse("Bad Data")
        response.status_code = 400
        return response

    s3 = boto3.client('s3')


    if not covfile is None:
        try:
            fileName = str(uuid.uuid1().hex) + ".png"
            s3.upload_fileobj(covfile, "openjukebutton", fileName, ExtraArgs={'ACL':'public-read'})
            coverUrl = "https://openjukebutton.s3.us-east-2.amazonaws.com/" + fileName
        except:
            response = HttpResponse("Couldn't upload cover art. Transaction not executed.")
            response.status_code = 400
            return response

    if not file is None:
        try:
            fileName = str(uuid.uuid1().hex) + ".mp3"
            s3.upload_fileobj(file, "openjukebutton", fileName, ExtraArgs={'ACL':'public-read'})
            url = "https://openjukebutton.s3.us-east-2.amazonaws.com/" + fileName
        except:
            response = HttpResponse("Couldn't upload song. Transaction not executed.")
            response.status_code = 400
            return response

    data = contract.encodeABI(fn_name="addSong", args=[url, coverUrl, title, artist, duration])

    #gasLimit = contract.functions.addSong(url, coverUrl, title, artist, duration).buildTransaction({'value': 80000000000000}).estimateGas() + 30000
    gasLimit = web3.eth.estimateGas(transaction={"to": address, "value": value, "data": data}) + 30000
    return HttpResponse(data + "%" + str(hex(gasLimit)) + "%" + str(hex(value)))

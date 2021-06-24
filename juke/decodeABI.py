from __future__ import unicode_literals
from web3 import Web3
from web3.middleware import geth_poa_middleware
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
import json
from django.conf import settings
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


    tx_hash = request.POST.get('tx_hash')
    if tx_hash == None or tx_hash == "":
        return HttpResponseBadRequest("Bad data")

    receipt = web3.eth.getTransactionReceipt(tx_hash)
    logs = contract.events.SongAdded().processReceipt(receipt)

    return HttpResponse(Web3.toJSON(logs))

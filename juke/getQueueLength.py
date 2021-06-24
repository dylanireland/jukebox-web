from django.http import HttpResponse
import os
from web3 import Web3
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
        return HttpResponse(contract.functions.getQueueDepth().call())
    except:
        return HttpResponse(-1)

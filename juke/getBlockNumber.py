from django.http import HttpResponse
from web3 import Web3
from .contract import Contract

# Create your views here.

def index(request):
    infuraUrl = Contract.getinfUrl()
    web3 = Web3(Web3.HTTPProvider(infuraUrl))
    return HttpResponse(web3.eth.blockNumber)

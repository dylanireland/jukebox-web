from .contract import Contract
import youtube_dl
from web3 import Web3
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
# Create your views here.
import boto3

def index(request):
    s3 = boto3.resource('s3')
    data = open('txt.txt', 'a')
    data.write("Bitch")
    s3.Bucket('openjukebutton').put_object(Key='txt.txt', Body=data)
    return HttpResponse("Should be done")

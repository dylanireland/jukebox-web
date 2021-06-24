from .contract import Contract
import youtube_dl
from web3 import Web3
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
# Create your views here.

def index(request):
    saveFromYoutube("https://www.youtube.com/watch?v=53_HPbH64_M", 760)



def saveFromYoutube(url, blockNumber):
    ydl_opts = {'format': 'bestaudio/best', 'extractaudio': True, 'audioformat': 'mp3', 'outtmpl': 'juke/static/songs/' + str(blockNumber) + '.mp3', 'noplaylist': True, 'nocheckcertificate':True, 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': '192'}],}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

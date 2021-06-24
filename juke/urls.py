from django.urls import path

from . import views
from . import app
from . import getQueueLength
from . import addSong
from . import getBlockNumber
from . import tests
from . import economics
from . import buildSongAdder
from . import decodeABI

urlpatterns = [
    path('', views.index, name='home'),
    path('app', app.index, name='app'),
    path('getQueueLength', getQueueLength.index, name='getQueueLength'),
    path('getBlockNumber', getBlockNumber.index, name='getBlockNumber'),
    path('addSong', addSong.index, name='addSong'),
    path('test', tests.index, name="tests"),
    path('economics', economics.index, name="economics"),
    path('buildSongAdder', buildSongAdder.index, name="buildSongAdder"),
    path('decodeABI', decodeABI.index, name="decodeABI")
]

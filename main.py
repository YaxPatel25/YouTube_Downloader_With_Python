import pytube
from pytube import YouTube
y=pytube.YouTube('https://www.youtube.com/watch?v=h3fUgOKFMNU')
#v=y.streams.first()
y.streams.first().download('C:/Users/hp/Downloads/YouTube/')
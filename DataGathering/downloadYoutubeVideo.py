import os
from pytube import YouTube

from pprint import pprint

print("Connecting to YouTube")
yt = YouTube("https://www.youtube.com/watch?v=V-u2jD7W3yU")

pprint(yt.get_videos())

fileName = 'ImpeachmentVote20160417'
yt.set_filename(fileName)

video = yt.get('mp4', '360p')
# video = yt.get('.3gp', '144p')

print("Downloading")
video.download(os.path.join("Temp",fileName,".mp4"))
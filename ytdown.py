#pip install pytube3
#if !work -> "pip install pytube==10.4.1"

from pytube import YouTube
import re

# Example: https://www.youtube.com/watch?v=ouwyCit_mRA
youtubelink = input("Youtube video URL to download: ")

# video.length || video.rating || video.views

#18 itag

try:
    video = YouTube(youtubelink)
    print("Downloading video...")
    video.streams.get_highest_resolution().download()
    print("Download Complete!")
except NameError:
    print("Video url is unavailable.")
except:
    print("URL needs to be valid.")


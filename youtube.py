from pytubefix import YouTube

 
url = "https://youtu.be/tR1ECf4sEpw?si=B1HSFi5tx6YrzFM1"
 
yt = YouTube(url)
print(yt.title)

audio = yt.streams.get_audio_only()
audio.download(mp3=(True))
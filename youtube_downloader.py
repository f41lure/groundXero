from pytube import YouTube

vid = input("Enter video url: ")

yt = YouTube(vid)

choice1 = input("Do you want to download audio or video? ")

if choice1 == "audio":
    x = yt.streams.filter(only_audio=True).all()
    x[1].download()

from pytube import YouTube

url = input("다운받을 youtube영상 URL 입력: ")
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download("./youtube_download_test")
from pytube import YouTube,Playlist
import os
from tqdm import tqdm
import moviepy.editor as mp
import librosa
from glob import glob 

DIR_ = os.path.join('audio_file')


if not os.path.exists(DIR_):
    os.mkdir(DIR_)

# youtube 플레이리스트 불러와서 mp3파일로 저장
def download_mp3(dir,pl):
    for no,link in tqdm(enumerate(pl)):
        yt = YouTube(link)
        stream = yt.streams.filter(file_extension='mp4').first()
        stream.download(output_path=dir,filename=str(no)+".mp4")
        tmp = os.path.join(dir,f"{no}.mp4")
        clip = mp.VideoFileClip(tmp)
        clip.audio.write_audiofile(os.path.join(dir,f"{no}.mp3"))
        clip.close()
        os.remove(tmp)

pl =Playlist("https://www.youtube.com/playlist?list=PLkO_NDjqDTzdUKeZZ5ou2GLLCBqtPoRB4")
download_mp3(DIR_,pl)


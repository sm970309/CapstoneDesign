from pytube import YouTube,Playlist
import os
from tqdm import tqdm
import moviepy.editor as mp
import librosa
from glob import glob 
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

DIR_ORIGIN = os.path.join('audio_file')
DIR_CLIPPED = os.path.join('clipped_audio_file')

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
def clip_mp3(input_wav,start,end):
    origin_sr =16000
    y, sr = librosa.load(input_wav, sr=origin_sr)
    print(f"original mp3 sr: {origin_sr}, length: {y.shape[0]/float(sr)}sec")
    new_y = y[round(start*sr):round(end*sr)]
    dir_name,mp3 = os.path.split(input_wav)
    output_path = os.path.join(DIR_CLIPPED,mp3)
    sf.write(output_path,new_y,16000)

if __name__ == '__main__':
    if not os.path.exists(DIR_ORIGIN): 
        os.mkdir(DIR_ORIGIN)
    if not os.path.exists(DIR_CLIPPED):
        os.mkdir(DIR_CLIPPED)
    # 플레이 리스트 입력
    pl =Playlist("https://www.youtube.com/playlist?list=PLkO_NDjqDTzdUKeZZ5ou2GLLCBqtPoRB4")

    # mp3파일 다운로드
    download_mp3(DIR_ORIGIN,pl)

    # mp3파일 clipping
    mp3_files = glob(os.path.join(DIR_ORIGIN,"*.mp3"))
    for mp3_file in mp3_files:
        start = int(input("start: "))
        end = int(input("end: "))
        clip_mp3(input_wav=mp3_file,start=start,end=end)
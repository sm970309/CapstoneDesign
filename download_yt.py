from pytube import YouTube,Playlist
import os
from tqdm import tqdm
import moviepy.editor as mp
from glob import glob 

DIR_ORIGIN = os.path.join('audio_file')

# youtube url 불러와서 mp4,mp3파일로 저장
def download_shorts(dir,url):
    if url.split('/')[-2]!='shorts':
        print('only shorts plz')
        return
    try:
        yt = YouTube(url)

        # download mp4
        stream = yt.streams.filter(file_extension='mp4').first()
        stream.download(output_path=dir,filename="tmp.mp4")

        # download mp3
        clip = mp.VideoFileClip(tmp)
        clip.audio.write_audiofile(os.path.join(dir,"tmp.mp3"))
        clip.close()
    except:
        print('error')

if __name__ == '__main__':
    if not os.path.exists(DIR_ORIGIN): 
        os.mkdir(DIR_ORIGIN)
    url = input("URL : ")
    download_shorts(DIR_ORIGIN,url)
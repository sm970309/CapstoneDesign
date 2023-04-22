from pytube import YouTube,Playlist
import os
from tqdm import tqdm
import moviepy.editor as mp
from glob import glob 

DIR_ORIGIN = os.path.join('audio_file')

# youtube url 불러와서 mp4,mp3파일로 저장
def download_shorts(url):
    if not os.path.exists(DIR_ORIGIN): 
        os.mkdir(DIR_ORIGIN)
    if url.split('/')[-2]!='shorts':
        print('only shorts plz')
        return 
    try:
        yt = YouTube(url)

        # download mp4
        stream = yt.streams.filter(file_extension='mp4').first()
        stream.download(output_path=DIR_ORIGIN,filename="tmp.mp4")
        
        # download mp3
        path = os.path.join(os.getcwd(),DIR_ORIGIN)
        clip = mp.VideoFileClip(os.path.join(path,'tmp.mp4'))

        audio_file_path = os.path.join(path,"tmp.mp3")
        clip.audio.write_audiofile(audio_file_path)
        clip.close()
        return audio_file_path
    except Exception as e:
        print("An error occurred:", e)
        return
    

if __name__ == '__main__':
    url = input("URL : ")
    download_shorts(url)
from urllib.request import HTTPSHandler
from pytube import YouTube
from pytube import Playlist
from time import sleep 
from moviepy import *
import os


#to download in audio form 
def audio_download(audio): 
    yt_obj = YouTube(str(audio))
    yt_obj.streams.get_audio_only().download(filename_prefix='mp3', output_path='songs\songs')
    print("downloaded")


# to download in video form 
def download_video(Video_name):
    yt_obj = YouTube(str(Video_name))
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    filters.get_highest_resolution().download()
    print("downloaded")



def downlaod_video_playlist(playlist_name):
    playlist = Playlist(str(playlist_name))


    for videos in playlist.videos: 
        try:  
            videos.streams.get_by_resolution(resolution='480p').download
            print(videos.title ,'                Downloaded in 480p')
        except :
            videos.streams.get_by_resolution(resolution='720p').download('video playlist')
            print(videos.title ,'                Downloaded in 720p')
        sleep(1)

#to download multible videos in playlist 
def downlaod_audio_playlist(playlist_name):
    playlist = Playlist(str(playlist_name))
    for videos in playlist.videos: 
        try:
            videos.streams.get_audio_only().download('songs' ,filename_prefix='mp3')
            print(videos.title ,'                Downloaded')

        except :
            print(videos.title, '           download failed')
         

def change_mp4_format():
    os.chdir('songs')
    x = os.listdir()
    for song in x :
        try:
            my_file = song
            base = os.path.splitext(my_file)[0]
            base1 = os.path.splitext(my_file)[1]
            print(base1)
            if base1 == '.mp4':
                my_file = os.rename('.mp3' + my_file, base + '.mp3')
                print('done')
            else : 
                pass
        except:
            print('error')


            
choice = input(("""\n
        to download audio press(1)\n
        to download video press(2) \n
        to download audio playlist press(3)\n
        to download video playlist press(4)
        

"""))


if int(choice) == 1 :
    x = input(str('enter URL '))
    audio_download(x)

if int(choice) == 2 :
    x = input(str('enter URL '))
    download_video(x)

if int(choice) == 3 :
    x = input(str('enter URL '))
    downlaod_audio_playlist(x)
    change_mp4_format()

if int(choice) == 4 :
    x = input(str('enter URL '))
    downlaod_video_playlist(x)



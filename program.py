from os import name
import tkinter
from tkinter.constants import BOTTOM, COMMAND, LEFT, RADIOBUTTON, RIGHT, TOP, X
from typing import Text
from pytube import YouTube
from pytube import Playlist
from time import sleep
from typing_extensions import IntVar 
import urllib3
from urllib.parse import unquote
from urllib.parse import quote
from PIL import Image
import os 
import spotdl


#enviroment of the gui app
top = tkinter.Tk()

#to add image to the background 
def back_image():
    my_image = Image.PhotoImage (Image.open('download'))
    label1 = tkinter.Label(image = my_image ).pack()



def enviroment():
    top.geometry('500x400')
    top.title('video downloader')







# radio buttons to determine the quality

L1 = tkinter.Label(top, text="playlist URL:", font=14)
L1.pack(side = LEFT)
E1 = tkinter.Entry(top, bd =8,insertwidth=2, width=30)
E1.pack(side = RIGHT)
#E1.insert(2,'enter url')

"""
E2 = tkinter.Entry(top ,bd =8,insertwidth=2, width=15)
E2.place(x=350, y= 0) 
E2.insert(1,'choose quality')
"""

'''
#quality list 
mb =tkinter.Menubutton(top,text='Quality List')
mb.menu = tkinter.Menu(mb)
mb['menu'] = mb.menu
mb.menu.add_command(tkinter.Label=='360p',command = lambda: print('this is option 1'))
mb.menu.add_command(tkinter.Label=='480p',command = lambda: print('this is option 1'))
mb.menu.add_command(tkinter.Label=='720p',command = lambda: print('this is option 1'))
mb.menu.add_command(tkinter.Label=='1080p',command = lambda: print('this is option 1'))
mb.place(x=350, y= 0) 
'''



def downloading():
    #adding indicator of the playlist videos's number 
    list2 = []
    mylabel = tkinter.Label(top, text = '\t\twait........downloading').place(x=100, y =300)
    x = E1.get()
    y = z.get()
    if y == 1:
        yt_obj = YouTube(str(x))
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        filters.get_highest_resolution().download()
        print("downloaded")

    if y == 2:
        yt_obj = YouTube(str(x))
        yt_obj.streams.get_audio_only().download(filename_prefix='mp3', output_path='songs')
        print("downloaded")


   
    if y == 3:
        playlist = Playlist(str(x))
        for videos in playlist.videos: 
           
            try:  
                videos.streams.get_by_resolution(resolution='480p').download
                print(videos.title ,'                Downloaded in 480p')
            except :
                videos.streams.get_by_resolution(resolution='720p').download('video playlist')
                print(videos.title ,'                Downloaded in 720p')
            sleep(1)
        tkinter.Label(top, text= '').place(x= 200, y= 250)



    if y == 4:
        playlist = Playlist(x)   
        for videos in playlist.videos: 
            y = videos.check_availability()
            if y == None:
                print(y)
                try:  
                    videos.streams.get_audio_only().download('songs')
                    print(videos.title ,'                Downloaded')
                    tkinter.Label(top, text= videos.title +'               \tDownloaded').place(x= 50, y= 100)
                except :
                    pass
                sleep(1)
            else :
                tkinter.Label(top, text= videos.title +'               unavilable').place(x= 50, y= 100)
    #spotify song 
    if y == 5:
        pass


    #spotify playlist
    if y == 6:
        pass


    #soundcloud song
    if y == 7:
        pass


    #soundcloud playlist
    if y == 8:
        pass


    # add here mp4 mp3 converter
    if y == 2 or y ==4 :
        os.chdir('songs')
        x = os.listdir()

        for song in x :
            try:
        
                my_file = song
                base = os.path.splitext(my_file)[0]
                base1 = os.path.splitext(my_file)[1]
                print(base1)
                if base1 == '.mp4':
                    my_file = os.rename(my_file, base + '.mp3')
                    print('done')
                else : 
                    pass
            except:
                print('error')
        


def but():
    print(z.get())

z =tkinter.IntVar()

#youtube 
but1= tkinter.Radiobutton(top,variable=z , value=1 ,text= 'video').place(x=150, y=0)
but2 = tkinter.Radiobutton(top,variable=z ,value=2 , text= 'audio').place(x=150, y=20)
but3= tkinter.Radiobutton(top,variable=z , value=3 ,text= 'video playlist').place(x=150, y=40)
but4 = tkinter.Radiobutton(top,variable=z ,value=4 , text= 'audio playlist').place(x=150, y=60)
'''#spotify
but5= tkinter.Radiobutton(top,variable=z , value=5 ,text= 'spotify song').place(x=250, y=0)
but6 = tkinter.Radiobutton(top,variable=z ,value=6 , text= 'spotify playlist').place(x=250, y=20)
#soundcloud`
but7= tkinter.Radiobutton(top,variable=z , value=7 ,text= 'soundcloud song').place(x=250, y=40)
but8 = tkinter.Radiobutton(top,variable=z ,value=8 , text= 'soundcloud playlist').place(x=250, y=60)



'''

#tkinter.Button(top, text='check',command=but).pack()
dowbottom = tkinter.Button(top, text = 'Download', command= lambda: [downloading()] , padx=60, pady= 20, font=14).place(x = 140, y = 300)



photo = tkinter.PhotoImage(file = "YT.png")
top.iconphoto(False, photo)








enviroment()
top.mainloop()


# adding quality change 
# add mp4 mp3 converter in the audio playlist 
# choose the place to save the downloaded stuff
# add indicator of dowqnloading staff 

import os 
"""


"""
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

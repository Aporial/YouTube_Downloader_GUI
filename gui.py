from tkinter import *
from tkinter import ttk

import ffmpeg
from pytube import YouTube
from pytube.cli import on_progress
import os

#os.remove('video.mp4')
#os.remove('audio.mp3')

root = Tk()
root.title('YouTube Downloader')
root.iconbitmap(default='favicon.ico')
root.geometry('400x500+750+250')
root.resizable(False, False)

##################



##################
def get_url():
    url = link.get()
    yt = YouTube(url)
    nam['text'] = yt.title
    print(url)



link = ttk.Entry()
link.pack(side='top', pady=5, ipady=5,)
link.place(x=110, y=8, height=25, width=280)


label = ttk.Label(text='Enter link:', font=('Intro', 12))
label.pack(side='top')
label.place(x=4, y=9)

fnd = ttk.Button(text='Find', command=get_url)
fnd.pack(side=TOP)
fnd.place(x=165, y=40)

hd = 'HD'
fhd = 'Full HD'
twok = '2K'
uhd = '4K'

hd_q = ttk.Radiobutton(text='720p', value=hd)
hd_q.pack()
hd_q.place(x=120, y=80)

fhd_q = ttk.Radiobutton(text='1080p', value=fhd)
fhd_q.pack()
fhd_q.place(x=230, y=80)

twok_q = ttk.Radiobutton(text='1440p', value=twok)
twok_q.pack()
twok_q.place(x=120, y=150)

uhd_q = ttk.Radiobutton(text='2160p', value=uhd)
uhd_q.pack()
uhd_q.place(x=230, y=150)

dwnl = ttk.Button(text='Download')
dwnl.pack(side=BOTTOM, fill='x', padx=10, pady=10, ipady=10)

bar = ttk.Progressbar()
bar.pack(side=BOTTOM, fill='x', padx=10)

nam0 = Label(text='Name: ')
nam0.pack()
nam0.place(x=180, y=375)

nam = Label()
nam.pack(side=BOTTOM)

#########################








root.mainloop()
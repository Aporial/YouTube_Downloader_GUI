from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

from threading import *

import ffmpeg
from pytube import YouTube
import os

##################

video_file = 'video.mp4'
audio_file = 'audio.mp3'

if os.path.exists(video_file):
    os.remove('video.mp4')
if os.path.exists(audio_file):
    os.remove('audio.mp3')

##################

root = Tk()
root.title('YouTube Downloader')
root.iconbitmap(default='./Core/favicon.ico')
root.geometry('400x500+750+250')
root.resizable(False, False)

##################
var = IntVar()
##################

def threading_url():
    t1=Thread(target=get_url)
    t1.start()
def threading_download():
    t2=Thread(target=download)
    t2.start()
def get_url():
    url = link.get()
    yt = YouTube(url)
    nam['text'] = yt.title

    fnd.configure(text='Finding...', state=DISABLED)

    if yt.streams.filter(video_codec="vp9", adaptive=True, res="720p"):
        hd_q.configure(state=NORMAL)
    if yt.streams.filter(video_codec="vp9", adaptive=True, res="1080p"):
        fhd_q.configure(state=NORMAL)
    if yt.streams.filter(video_codec="vp9", adaptive=True, res="1440p"):
        twok_q.configure(state=NORMAL)
    if yt.streams.filter(video_codec="vp9", adaptive=True, res="2160p"):
        uhd_q.configure(state=NORMAL)

    fnd.configure(text='Find', state=NORMAL)
    dwnl.configure(state=NORMAL)
def selected():
    var.get()

def download():
    url = link.get()
    yt = YouTube(url)
    dwnl.configure(text='Downloading...', state=DISABLED)
    fnd.configure(state=DISABLED)
    link.configure(state=DISABLED)
    hd_q.configure(state=DISABLED)
    fhd_q.configure(state=DISABLED)
    twok_q.configure(state=DISABLED)
    uhd_q.configure(state=DISABLED)
    sell = var.get()
    if sell == 1:
        yt.streams.filter(res="720p", progressive=False).first().download(filename="video.mp4")
        video = ffmpeg.input("video.mp4")
    if sell == 2:
        yt.streams.filter(res="1080p", progressive=False).first().download(filename="video.mp4")
        video = ffmpeg.input("video.mp4")
    if sell == 3:
        yt.streams.filter(res="1440p", progressive=False).first().download(filename="video.mp4")
        video = ffmpeg.input("video.mp4")
    if sell == 4:
        yt.streams.filter(res="2160p", progressive=False).first().download(filename="video.mp4")
        video = ffmpeg.input("video.mp4")
    bar.configure(value=33)
    yt.streams.filter(abr="160kbps", progressive=False).first().download(filename="audio.mp3")
    audio = ffmpeg.input("audio.mp3")
    bar.configure(value=66)
    ffmpeg.output(video, audio, 'Download/download_video.mp4', vcodec='copy', acodec='copy', loglevel="quiet").run()
    var.set(0)
    link.configure(state=NORMAL)
    dwnl.configure(text='Download', state=NORMAL)
    fnd.configure(state=NORMAL)
    bar.configure(value=75)
    bar.configure(value=0)
    showinfo(title='Download Status', message='Download Completed!')
    os.system('start Download')
    os.remove('video.mp4')
    os.remove('audio.mp3')

link = ttk.Entry()
link.pack(side='top', pady=5, ipady=5,)
link.place(x=110, y=8, height=25, width=280)

label = ttk.Label(text='Enter link:', font=('Intro', 12))
label.pack(side='top')
label.place(x=4, y=9)

fnd = ttk.Button(text='Find', command=threading_url)
fnd.pack(side=TOP)
fnd.place(x=165, y=40)

hd_q = ttk.Radiobutton(text='HD', state=DISABLED, value=1, variable=var, command=selected)
hd_q.pack()
hd_q.place(x=120, y=80)

fhd_q = ttk.Radiobutton(text='Full HD', state=DISABLED, value=2, variable=var, command=selected)
fhd_q.pack()
fhd_q.place(x=230, y=80)

twok_q = ttk.Radiobutton(text='2K', state=DISABLED, value=3, variable=var, command=selected)
twok_q.pack()
twok_q.place(x=120, y=150)

uhd_q = ttk.Radiobutton(text='4K', state=DISABLED, value=4, variable=var, command=selected)
uhd_q.pack()
uhd_q.place(x=230, y=150)

dwnl = ttk.Button(text='Download', command=threading_download, state=DISABLED)
dwnl.pack(side=BOTTOM, fill='x', padx=10, pady=10, ipady=10)

bar = ttk.Progressbar(mode='determinate', maximum=100, value=0)
bar.pack(side=BOTTOM, fill='x', padx=10)


nam0 = Label(text='Name: ')
nam0.pack()
nam0.place(x=180, y=375)

nam = Label(justify=LEFT, width=50)
nam.pack(side=BOTTOM)

#########################

root.mainloop()
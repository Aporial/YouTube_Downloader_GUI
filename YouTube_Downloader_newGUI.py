from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
from PIL import ImageTk, Image
import requests

from threading import *

import ffmpeg
from pytube import YouTube
import os

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

##################

video_file = 'video.mp4'
audio_file = 'audio.mp3'
logo_file = 'logo.jpg'

if os.path.exists(video_file):
    os.remove('video.mp4')
if os.path.exists(audio_file):
    os.remove('audio.mp3')
if os.path.exists(logo_file):
    os.remove('logo.jpg')
##################


root = customtkinter.CTk()
root.title('YouTube Downloader')
root.geometry('400x500+750+250')
root.wm_iconbitmap(default='./Core/favicon.ico')
root.resizable(False, False)

##################
var = IntVar()


##################

def threading_url():
    t1 = Thread(target=get_url)
    t1.start()


def threading_download():
    t2 = Thread(target=download)
    t2.start()


def get_url():
    url = link.get()
    yt = YouTube(url)
    title = yt.title
    nam.configure(text=title)
    logo_url = yt.thumbnail_url.replace('sddefault.jpg', 'maxresdefault.jpg')
    response = requests.get(logo_url)
    open("logo.jpg", "wb").write(response.content)
    logo = customtkinter.CTkImage(dark_image=Image.open('logo.jpg'), size=(380, 200))
    label_img.configure(image=logo)

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
    if sell == 2:
        yt.streams.filter(res="1080p", progressive=False).first().download(filename="video.mp4")
    if sell == 3:
        yt.streams.filter(res="1440p", progressive=False).first().download(filename="video.mp4")
    if sell == 4:
        yt.streams.filter(res="2160p", progressive=False).first().download(filename="video.mp4")
    video = ffmpeg.input("video.mp4")
    bar.configure(value=33)
    yt.streams.filter(abr="160kbps", progressive=False).first().download(filename="audio.mp3")
    audio = ffmpeg.input("audio.mp3")
    bar.configure(value=66)
    ffmpeg.output(video, audio, 'Download/downloaded_video.mp4', vcodec='copy', acodec='copy', loglevel="quiet").run()
    var.set(0)
    link.configure(state=NORMAL)
    dwnl.configure(text='Download', state=NORMAL)
    fnd.configure(state=NORMAL)
    bar.configure(value=75)
    bar.configure(value=0)
    old_filename = yt.title
    new_filename = old_filename.translate(str.maketrans(' ', ' ', '\/:*?"<>|'))
    os.rename('Download/downloaded_video.mp4', 'Download/' + new_filename + '.mp4')
    showinfo(title='Download Status', message='Download Completed!')
    os.system('start Download')
    os.remove('video.mp4')
    os.remove('audio.mp3')
    os.remove('logo.jpg')

def keypress(event):
    if event.keycode == 86:
        event.widget.event_generate("<<Paste>>")
    elif event.keycode == 67:
        event.widget.event_generate("<<Copy>>")
    elif event.keycode == 88:
        event.widget.event_generate("<<Cut>>")
    elif event.keycode == 65535:
        event.widget.event_generate("<<Clear>>")
    elif event.keycode == 65:
        event.widget.event_generate("<<SelectAll>>")


root.bind("<Control-KeyPress>", keypress)

link = customtkinter.CTkEntry(master=root)
link.pack(side='top', pady=5, ipady=5, )
link.place(x=110, y=8, height=25, width=280)

label = customtkinter.CTkLabel(master=root, text='Enter link:', font=('Arial', 20))
label.pack(side='top')
label.place(x=12, y=6)

fnd = customtkinter.CTkButton(master=root, text='Find', font=('Arial', 18), command=threading_url)
fnd.pack(side=TOP)
fnd.place(x=130, y=40)

hd_q = customtkinter.CTkRadioButton(master=root, text='HD', font=('Arial', 18), state=DISABLED, value=1, variable=var,
                                    command=selected)
hd_q.pack()
hd_q.place(x=120, y=80)

fhd_q = customtkinter.CTkRadioButton(master=root, text='Full HD', font=('Arial', 18), state=DISABLED, value=2,
                                     variable=var, command=selected)
fhd_q.pack()
fhd_q.place(x=230, y=80)

twok_q = customtkinter.CTkRadioButton(master=root, text='2K', font=('Arial', 18), state=DISABLED, value=3, variable=var,
                                      command=selected)
twok_q.pack()
twok_q.place(x=120, y=130)

uhd_q = customtkinter.CTkRadioButton(master=root, text='4K', font=('Arial', 18), state=DISABLED, value=4, variable=var,
                                     command=selected)
uhd_q.pack()
uhd_q.place(x=230, y=130)

dwnl = customtkinter.CTkButton(master=root, text='Download', font=('Arial', 18), command=threading_download,
                               state=DISABLED)
dwnl.pack(side=BOTTOM, fill='x', padx=10, pady=10, ipady=10)

bar = ttk.Progressbar(mode='determinate', maximum=100, value=0)
bar.pack(side=BOTTOM, fill='x', padx=10)

nam0 = customtkinter.CTkLabel(master=root, text='Name: ', font=('Arial', 14))
nam0.pack()
nam0.place(x=180, y=360)

nam = customtkinter.CTkLabel(master=root, justify=RIGHT, width=40, text='', font=('Arial', 14))
nam.pack(side=BOTTOM)
nam.place(x=10, y=380)



label_img = customtkinter.CTkLabel(master=root, text='')
label_img.pack()
label_img.place(x=10, y=160)


#########################
def on_closing():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

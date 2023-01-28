from tkinter import *
from tkinter import ttk

root = Tk()
root.title('YouTube Downloader')
root.iconbitmap(default='favicon.ico')
root.geometry('400x500+750+250')
root.resizable(False, False)

##################

def click():
    print('hello')


##################

link = ttk.Entry()
link.pack(side='top', pady=5, ipady=5,)
link.place(x=110, y=8, height=25, width=280)


label = ttk.Label(text='Enter link:', font=('Intro', 12))
label.pack(side='top')
label.place(x=4, y=9)

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

dwnl = ttk.Button(text='Download', command=click)
dwnl.pack(side=BOTTOM, fill='x', padx=10, pady=10, ipady=10)

fnd = ttk.Button(text='Find')
fnd.pack(side=TOP)
fnd.place(x=165, y=40)

bar = ttk.Progressbar()
bar.pack(side=BOTTOM, fill='x', padx=10)

nam = Label(text='Name: ')
nam.pack(side=BOTTOM)

#########################








root.mainloop()
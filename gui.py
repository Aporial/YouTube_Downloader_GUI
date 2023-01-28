from tkinter import *
from tkinter import ttk

root = Tk()
root.title('YouTube Downloader')
root.iconbitmap(default='favicon.ico')
root.geometry('400x500+750+250')
root.resizable(False, False)

link = ttk.Entry()
link.pack(side='top', pady=5, ipady=5,)
link.place(x=93, y=8, height=25, width=300)

label = ttk.Label(text='Enter link:')
label.pack(side='top')
label.place(x=10, y=10)

qua = ttk.Checkbutton(text='720p')
qua.pack()
qua.place(x=5, y=50)

qua = ttk.Checkbutton(text='1080p')
qua.pack()
qua.place(x=100, y=50)

qua = ttk.Checkbutton(text='1440p')
qua.pack()
qua.place(x=5, y=100)

qua = ttk.Checkbutton(text='2160p')
qua.pack()
qua.place(x=100, y=100)

btn = ttk.Button(text='Download')
btn.pack(side=BOTTOM, fill='x', padx=10, pady=10, ipady=10)











root.mainloop()
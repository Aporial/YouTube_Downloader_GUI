import tkinter as tk
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
from pytube import YouTube

root = tk.Tk()
url = 'https://www.youtube.com/watch?v=ukoPSg8H9Uc'
yt = YouTube(url)
high_resolution_thumbnail_url = yt.thumbnail_url.replace('sddefault.jpg', 'maxresdefault.jpg')
u = urllib.request.urlopen(high_resolution_thumbnail_url)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
im = im.resize((1280, 720), Image.LANCZOS)
photo = ImageTk.PhotoImage(im)

button = tk.Label(image=photo, width=1280, height=720)
button.image = photo
button.pack()
print(yt.thumbnail_url)
root.mainloop()
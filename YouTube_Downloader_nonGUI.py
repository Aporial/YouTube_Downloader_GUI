import ffmpeg
from pytube import YouTube
from pytube.cli import on_progress
import os

video_file = 'video.mp4'
audio_file = 'audio.mp3'

if os.path.exists(video_file):
    os.remove('video.mp4')
if os.path.exists(audio_file):
    os.remove('audio.mp3')

url = input('Video link: ')
yt = YouTube(url, on_progress_callback=on_progress)

print('Name: ', yt.title)
print('Wait. Processing video quality...')
for stream in yt.streams.filter(video_codec="vp9", adaptive=True, res="720p"):
    print('1.', stream.resolution, 'HD')
for stream in yt.streams.filter(video_codec="vp9", adaptive=True, res="1080p"):
    print('2.', stream.resolution, 'Full HD')
for stream in yt.streams.filter(video_codec="vp9", adaptive=True, res="1440p"):
    print('3.', stream.resolution, '2K')
for stream in yt.streams.filter(video_codec="vp9", adaptive=True, res="2160p"):
    print('4.', stream.resolution, '4K')

ress = input('Select the video quality: ')
if ress == '1':
    yt.streams.filter(res="720p", progressive=False).first().download(
        filename="video.mp4")
    video = ffmpeg.input("video.mp4")
if ress == '2':
    yt.streams.filter(res="1080p", progressive=False).first().download(
        filename="video.mp4")
    video = ffmpeg.input("video.mp4")
if ress == '3':
    yt.streams.filter(res="1440p", progressive=False).first().download(
        filename="video.mp4")
    video = ffmpeg.input("video.mp4")
if ress == '4':
    yt.streams.filter(res="2160p", progressive=False).first().download(
        filename="video.mp4")
    video = ffmpeg.input("video.mp4")

yt.streams.filter(abr="160kbps", progressive=False).first().download(
    filename="audio.mp3")
audio = ffmpeg.input("audio.mp3")

print('Wait. Video is being processed...')

ffmpeg.output(video, audio, 'download_video.mp4', vcodec='copy',
              acodec='copy', loglevel="quiet").run()
os.remove('video.mp4')
os.remove('audio.mp3')

print('Video uploaded!')

exit()

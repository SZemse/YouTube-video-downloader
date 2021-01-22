from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('600x400')
root.configure(bg = 'antique white')
root.title('Youtube Video Downloader')
url = StringVar()

Label(root, text='Youtube Video Downloader', font = 'Courier 25 bold', bg = 'antique white' ).pack()

Label(root, text='Paste URL Here', font = 'Courier 15 bold', bg = 'antique white').place(x = 200, y = 100)
url_enter = Entry(root, width = 80, textvariable = url).place(x = 53, y = 140)

def Download():
    video_url = YouTube(str(url.get()))
    video = video_url.streams.first()
    video.download()
    Label(root, text = 'Video is downloaded!', font = 'Courier 15 bold',  bg = 'antique white' ).place(x = 180, y = 250)

Button(root, text='Download', font = 'Courier 15 bold', bg = 'MediumOrchid2', padx = 2, command = Download).place(x = 235, y = 190)


root.mainloop()
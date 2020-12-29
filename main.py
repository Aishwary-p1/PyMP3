import pygame
import tkinter as tk
import os
from tkinter.filedialog import askdirectory
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class OPEN(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("PyMP3")
        self.style = Style()
        self.style.theme_use("default")

        #frame = Frame(self, relief=RAISED, borderwidth=1)
        #frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)
        
        closeButton = Button(self, text="CLOSE", command=window.destroy)
        closeButton.pack(side=RIGHT, padx=5, pady=5)

        Button2 = Button(self, text="STOP", command=stop)
        Button2.pack(side=RIGHT, padx=5, pady=5)

        Button4 = Button(self, text="UNPAUSE", command=unpause)
        Button4.pack(side=RIGHT, padx=5, pady=5)

        Button3 = Button(self, text="PAUSE", command=pause)
        Button3.pack(side=RIGHT, padx=5, pady=5)

        Button1 = Button(self, text="PLAY", command=play)
        Button1.pack(side=RIGHT, padx=5, pady=5)


#Play Music
def play():
    pygame.mixer.music.load(play_list.get(tk.ACTIVE))
    var.set(play_list.get(tk.ACTIVE))
    pygame.mixer.music.play()

#Stop Music
def stop():
    pygame.mixer.music.stop()

#Pause Music
def pause():
    pygame.mixer.music.pause()

#Resume Music
def unpause():
    pygame.mixer.music.unpause()

#Change Window Size and open Directory
def open():
    pass

window = tk.Tk()
#Tkinter Icon
photo = tk.PhotoImage(file = "C:\\Users\\aishw\\Desktop\\Project\\mp3\\mp3-icon.png")
window.iconphoto(False, photo)
window.title("Music Player")
window.geometry("162x74")
#window.geometry("562x274")


#Open Folder Button
open_btn = Button(window, text = 'OPEN FOLDER', command = open)  
open_btn.pack(side="top", anchor="nw", padx=5, pady=5)

#New Frame
window.geometry("562x314")
dir = askdirectory()
os.chdir(dir)
songs = os.listdir()
play_list = tk.Listbox(window, font="Times 12 bold", bg="pale turquoise", selectmode=tk.SINGLE)
for item in songs:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()

var = tk.StringVar() 
song_title = tk.Label(window, font="Times 12 bold", textvariable=var)

song_title.pack()

play_list.pack(fill="both", expand="yes")
app = OPEN()

pass

window.mainloop()
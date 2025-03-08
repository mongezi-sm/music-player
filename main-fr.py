# This is my first public project, a music player. It is still under development.
# The original source code is from https://towardsdatascience.com/how-to-build-an-mp3-music-player-with-python-619e0c0dcee2,
# but I am planning on making changes and differentiating it from the original.

from tkinter.constants import ANCHOR
import pygame
import tkinter as tkr
from tkinter import *
from tkinter.filedialog import askdirectory
import os
from tkinter.ttk import *
import audio_metadata
from PIL import ImageTk, Image
from io import BytesIO
import eyed3

music_player = tkr.Tk()
music_player.title("Mo's Music Player")
music_player.geometry("640x480")

# Scrollbar tings
scrollbar = Scrollbar(music_player)
scrollbar.pack(side = RIGHT, fill=Y )

directory = askdirectory() # Change this line into a button
os.chdir(directory)
song_list = os.listdir() # Returns the list of files

play_list = tkr.Listbox(music_player, font="Arial 12", bg="white", selectmode=tkr.SINGLE)

for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

# Writing functions to control the music player

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

# Creating the buttons that will control the interface

btnPlay = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text = "play", command=play, bg="blue", fg="white")
btnStop = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text = "stop", command=stop, bg="blue", fg="white")
btnPause = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text = "pause", command=pause, bg="blue", fg="white")
btnUnpause = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text = "unpause", command=unpause, bg="blue", fg="white")

# Line that displays the current playing song
# Note: add picture? Fingers crossed it works lol

now_playing = tkr.Frame(music_player, width=480, height=200, bg="black")
now_playing.pack_propagate(False)
now_playing.pack()

var = tkr.StringVar()
song_title = tkr.Label(now_playing, font="Arial 12", textvariable=var)
metadata = audio_metadata.load(play_list.get(tkr.ACTIVE))
curr_audio = eyed3.load(play_list.get(tkr.ACTIVE))
song_title = tkr.Label(now_playing, font="Arial 12", textvariable=var)
song_title = tkr.Label(now_playing, font="Arial 12", textvariable=var)
song_title = tkr.Label(now_playing, font="Arial 12", textvariable=var)
artwork = metadata.pictures[0].data
stream = BytesIO(artwork)

# Create frame for Now Playing section




# Display picture:

canvas = tkr.Canvas(now_playing, width = 150, height = 150)
canvas.pack()
img = ImageTk.PhotoImage(Image.open(stream))
canvas.create_image(0,0, image=img)
canvas.place(x=20, y=30)


song_title.pack()
btnPlay.pack(fill="x")
btnStop.pack(fill="x")
btnPause.pack(fill="x")
btnUnpause.pack(fill="x")
btnPlay.pack(fill="x")
play_list.pack(fill="both", expand="yes")
play_list.mainloop()

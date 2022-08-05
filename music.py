from os import remove
from signal import pause
from tkinter import *
from tkinter.tix import COLUMN
from tokenize import maybe
from tracemalloc import stop
from turtle import width
from tkinter import filedialog
import pygame

root = Tk()
root.title('Music Player')
root.geometry("500x300")


#initialize pygame mixer
pygame.mixer.init()

#add song function
def add_song():
    song = filedialog.askopenfilename(initialdir='/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Songs', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))
    
    #strip out the directory info and .mp3 extension from the song name
    song = song.replace("/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Songs/", "")
    song = song.replace(".mp3", "")
    
    #add song to listbox
    song_box.insert(END, song)

#add many songs to playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Songs', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))

    #loop through song list and replace directory info and mp3
    for song in songs:
        song = song.replace("/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Songs/", "")
        song = song.replace(".mp3", "")

        #insert into playlist
        song_box.insert(END, song)

#delete a song
def delete_songs():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

#delete all songs
def delete_all_songs():
    song_box.delete(0, END)

    #stop music if its playing
    pygame.mixer.music.stop()

#play selected song
def play():
    song = song_box.get(ACTIVE)
    song = f'/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Songs/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#play previous song in the playlist
def previous_song():
    #get current song tuple number
    next_one = song_box.curselection()

    #add one to the current song
    next_one = next_one[0]-1

    #grab song title from playlist
    song = song_box.get(next_one)

    #add directory structure and mp3 to song title 
    song = f'/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Songs/{song}.mp3'

    #load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #clear active bar in playlist listbox
    song_box.selection_clear(0, END)

    #activate new song bar
    song_box.activate(next_one)

    #set active bar to next song
    song_box.selection_set(next_one, last = None)



#stop playing current song
def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)

#play the next song in the playlist
def next_song():
    #get current song tuple number
    next_one = song_box.curselection()

    #add one to the current song
    next_one = next_one[0]+1

    #grab song title from playlist
    song = song_box.get(next_one)

    #add directory structure and mp3 to song title 
    song = f'/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Songs/{song}.mp3'

    #load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #clear active bar in playlist listbox
    song_box.selection_clear(0, END)

    #activate new song bar
    song_box.activate(next_one)

    #set active bar to next song
    song_box.selection_set(next_one, last = None)
    
#pause and unpause current song
def pause(is_paused):

    global paused
    paused = is_paused

    if paused:
        #unpause
        pygame.mixer.music.unpause() #unpause
        paused = False
    else:
        pygame.mixer.music.pause() #pause
        paused=True

#create global pause variable
global paused
paused = False

#create playlist box
song_box = Listbox(root, bg = "black", fg = "green", width=50, selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)

#create player control buttons
back_btn_img = PhotoImage(file='/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Images/back50.png')
forward_btn_img = PhotoImage(file='/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Images/forward50.png')
play_btn_img = PhotoImage(file='/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Images/play50.png')
pause_btn_img = PhotoImage(file='/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Images/pause50.png')
stop_btn_img = PhotoImage(file='/Users/dhruvitvanani/Desktop/Py/MusicPlayer/Images/stop50.png')


#Create player control Frames
controls_frame = Frame(root)
controls_frame.pack()

#create player control buttons
back_button = Button(controls_frame, image=back_btn_img , borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command = play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)


back_button.grid(row=0, column=0, padx =10)
forward_button.grid(row=0, column=1, padx =10)
play_button.grid(row=0, column=2, padx =10)
pause_button.grid(row=0, column=3, padx =10)
stop_button.grid(row=0, column=4, padx =10)

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playlist", command=add_song)


#add many songs to playlist
add_song_menu.add_command(label="Add many song to playlist", command=add_many_songs)


#create a delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a song from playlist", command=delete_songs)
remove_song_menu.add_command(label="Delete all songs from playlist", command=delete_all_songs)

root.mainloop()

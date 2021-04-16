"""
    Dependencies : tkinter, playsound, vext & vext.gi
    INSTALLATION : pip install playsound vext vext.gi
"""
import time
from tkinter import *
from tkinter import filedialog
import pygame
from pygame.locals import *
import sys
import mutagen
from mutagen.mp3 import MP3
from pygame import movie
from playsound import playsound

# initialize pygame
pygame.mixer.init()

app = Tk()
app.title("Magpiny Music Player")
app.geometry("700x620+100+100")


# Music timer function
def get_time():
    current_time = pygame.mixer.music.get_pos()/1000
    new_curr_time = time.strftime("%M:%S", time.gmtime(current_time))
    status_bar.config(text=new_curr_time)
    status_bar.after(1000, get_time)


# add song function
def add_song():
    song = filedialog.askopenfilename(initialdir="/home/magpiny/Music/BLUES/", title="Pick a Song",
                                      filetypes=(("mp3 files", "*.ogg"),))
    song = song.replace("/home/magpiny/Music/BLUES/", "")
    song = song.replace(".ogg", "")
    playlist_box.insert(END, song)


def add_many_song():
    songs = filedialog.askopenfilenames(initialdir="/home/magpiny/Music/BLUES", title="Pick Songs",
                                        filetypes=(("mp3 files", "*.ogg"),))
    for song in songs:
        song = song.replace("/home/magpiny/Music/BLUES/", "")
        song = song.replace(".ogg", "")
        playlist_box.insert(END, song)


# delete songs
def delete_song():
    playlist_box.delete(ANCHOR)


def delete_all_songs():
    playlist_box.delete(0, END)


# Media control buttons functions
def back():
    # Get the current song
    nxt = playlist_box.curselection()
    next_one = nxt[0] - 1
    # Grab the song from the playlist
    song = playlist_box.get(next_one)
    # Get the song title
    song = f"/home/magpiny/Music/BLUES/{song}.ogg"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Clear active bar
    playlist_box.select_clear(0, END)
    # And move it to the next line
    playlist_box.activate(next_one)
    # Set the active bar to the next lin
    playlist_box.select_set(next_one, last=None)


global paused
# paused passed as a parameter to button in the lambda function call
paused = True


def pause(is_paused):
    global paused
    paused = True
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


global running
running = False


def play(playing):
    # reconstruct the replaced string add_song and add_all_songs above
    pygame.init()
    global running
    # running = True
    running = playing
    song = playlist_box.get(ACTIVE)
    song = f"/home/magpiny/Music/BLUES/{song}.ogg"
    # mylabel.config(text=song)

    try:
        # load songs with pygame
        pygame.mixer.music.load(song)
        # playsound(song)
        # play songs with pygame
        pygame.mixer.music.play(0)
        get_time()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    mylabel.config(text="The song ended!")
                    running = False
                    pygame.quit()
                    sys.exit()

    except Exception as error:
        mylabel.config(text=error)
        time.sleep(3000)
        pygame.quit()


def next_song():
    # Get the current song
    nxt = playlist_box.curselection()
    next_one = nxt[0]+1
    # Grab the song from the playlist
    song = playlist_box.get(next_one)
    # Get the song title
    song = f"/home/magpiny/Music/BLUES/{song}.ogg"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Clear active bar
    playlist_box.select_clear(0, END)
    # And move it to the next line
    playlist_box.activate(next_one)
    # Set the active bar to the next lin
    playlist_box.select_set(next_one, last=None)


def stop():
    pygame.mixer.music.fadeout(3000)
    # pygame.mixer.music.stop()
    playlist_box.select_clear(ACTIVE)


my_menu = Menu(app, )
app.config(menu=my_menu)

submenu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Song to Playlist", menu=submenu)
submenu.add_command(label="Add a song", command=add_song)
submenu.add_command(label="Add Many Songs", command=add_many_song)
submenu.add_command(label="Delete Song", command=delete_song)
submenu.add_command(label="Delete All Songs", command=delete_all_songs)
submenu.add_command(label="Exit", command=quit)

# List box
playlist_box = Listbox(app, fg="#3498db", bg="#34495e", bd=10, width=80, height=26, selectbackground="#2980b9",
                       selectforeground="red")

# Frame for the buttons
control_frame = Frame(app, bd=0)

# Define image buttons
back_btn_img = PhotoImage(file="./images/back-arrow.png")
pause_btn_img = PhotoImage(file="./images/pause.png")
play_btn_img = PhotoImage(file="./images/player2.png")
stop_btn_img = PhotoImage(file="./images/stop.png")
forward_btn_img = PhotoImage(file="./images/forward.png")

# Media control buttons
back_btn = Button(control_frame, image=back_btn_img, borderwidth=0, command=back)
play_btn = Button(control_frame, image=play_btn_img, borderwidth=0, command=lambda: play(running))
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
forward_btn = Button(control_frame, image=forward_btn_img, borderwidth=0, command=next_song)
stop_btn = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)

# Extra Label
mylabel = Label(app, text="", fg="#d81b60")
mylabel2 = Label(app, text="", fg="red")

# Status bar
status_bar = Label(text="Status bar", bd=1, relief=RAISED, anchor=CENTER)
# pack all your widgets here
playlist_box.pack(pady=20)
control_frame.pack(pady=10)

# pack buttons
back_btn.pack(side="left", padx=5)
pause_btn.pack(side="left", padx=5)
play_btn.pack(side="left", padx=5)
forward_btn.pack(side="left", padx=5)
stop_btn.pack(side="left")

status_bar.pack(ipady=4, ipadx=4)
mylabel.pack(side="right", ipady=10, pady=10)
mylabel2.pack(side="bottom", ipady=10, pady=15)

app.mainloop()

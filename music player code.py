from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import sys 

#add many songs to the playlist of python mp3 player
def addsongs():
    #to open a file  
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for s in temp_song:
        s=s.replace("D:\anitha\Desktop\mp3\music\Summertime-Sadness(PaglaSongs).mp3","")
    songs_list.insert(END,s)
     
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
    
    
def Play():
    song=songs_list.get(ACTIVE)
    song=f'{song}'
    mixer.music.load(song)
    mixer.music.play()
#to pause the song 
def Pause():
    mixer.music.pause()
#to stop the  song 
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)
#to resume the song
def Resume():
    mixer.music.unpause()
#Function to navigate from the current song
def Previous():
   # Get the selected song index
    current_index = songs_list.curselection()[0]

    # Check if there's a previous song to play
    if current_index > 0:
        # Get the previous song index
        previous_index = current_index - 1

        # Get the previous song from the list
        previous_song = songs_list.get(previous_index)

        # Play the previous song
        mixer.music.load(previous_song)
        mixer.music.play()

        # Clear the selection in the listbox
        songs_list.selection_clear(0, END)

        # Activate and select the previous song
        songs_list.activate(previous_index)
        songs_list.selection_set(previous_index)
def Next():
   # Get the selected song index
    current_index = songs_list.curselection()[0]

    # Check if there's a next song to play
    if current_index < songs_list.size() - 1:
        # Get the next song index
        next_index = current_index + 1

        # Get the next song from the list
        next_song = songs_list.get(next_index)

        # Play the next song
        mixer.music.load(next_song)
        mixer.music.play()

        # Clear the selection in the listbox
        songs_list.selection_clear(0, END)

        # Activate and select the next song
        songs_list.activate(next_index)
        songs_list.selection_set(next_index)

root=Tk()
root.title('Python MP3 Music player App ')
#initialize mixer 
mixer.init()
#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=9)
#font is defined which is to be used for the button font 
defined_font = font.Font(family='Helvetica')
#play button
play_button=Button(root,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)
#pause button 
pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)
#stop button
stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)
#resume button
Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)
#previous button
previous_button=Button(root,text="Prev",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)
#nextbutton
next_button=Button(root,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)
#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)

root.mainloop()
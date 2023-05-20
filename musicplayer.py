def UnMuteMusic():
    global CurrentVolume
    root.UnMuteButton.grid_remove()
    root.MuteButton.grid()
    mixer.music.set_volume(CurrentVolume)

def MuteMusic():
    global CurrentVolume
    root.MuteButton.grid_remove()
    root.UnMuteButton.grid()
    CurrentVolume = mixer.music.get_volume()
    mixer.music.set_volume(0)

def ResumeMusic():
    mixer.music.unpause()
    root.ResumeButton.grid_remove
    root.PauseButton.grid()
    AudioStatusLabel.configure(text="Playing...")

def IncreaseVolume():
    Volume = mixer.music.get_volume()
    mixer.music.set_volume(Volume+0.06)
    ProgressBarVolumeLevel.configure(text="{}%".format(int(mixer.music.get_volume()*100)))
    ProgressBarVolume["value"]=mixer.music.get_volume()*100

def DecreaseVolume():
    Volume = mixer.music.get_volume()
    mixer.music.set_volume(Volume-0.06)
    ProgressBarVolumeLevel.configure(text="{}%".format(int(mixer.music.get_volume()*100)))
    ProgressBarVolume["value"]=mixer.music.get_volume()*100

def StopMusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text="Stopped...")

def PauseMusic():
    mixer.music.pause()
    root.PauseButton.grid_remove
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text="Paused...")

def PlayMusic():
    global AudioTrack
    audio = AudioTrack.get()
    mixer.music.load(audio)
    ProgressBarLabel.grid()
    ProgressBarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressBarVolume["value"]=40
    ProgressBarVolumeLevel["text"]="40%"
    root.MuteButton.grid()
    mixer.music.play()
    AudioStatusLabel.configure(text="Playing...")

    Song = MP3(audio)
    TotalSongLength = int(Song.info.length)
    ProgressBarMusic["maximum"]=TotalSongLength
    ProgressBarMusicEndTimeLabel.configure(text="{}".format(str(datetime.timedelta(seconds=TotalSongLength))))
    
    def ProgressBarMusictick():
        CurrentSongLength = mixer.music.get_pos()//1000
        ProgressBarMusic["value"] = CurrentSongLength
        ProgressBarMusicBegTimeLabel.configure(text="{}".format(str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressBarMusic.after(2,ProgressBarMusictick)
    ProgressBarMusictick()

def MusicURL():
    link = filedialog.askopenfilename()
    AudioTrack.set(link)
def CreateWidthes():
    global its_search,its_play,its_pause,its_stop,its_VolumeIncrease,its_VolumeDecrease,its_Resume,its_Mute,its_UnMute
    global AudioStatusLabel,ProgressBarLabel,ProgressBarVolume,ProgressBarVolumeLevel,ProgressBarMusic,ProgressBarMusicLabel
    global ProgressBarMusicBegTimeLabel,ProgressBarMusicEndTimeLabel
    #images
    its_search = PhotoImage(file = "icons8-search-48.png")
    its_play = PhotoImage(file = "icons8-play-64.png")
    its_pause = PhotoImage(file = "icons8-pause-48.png")
    its_stop = PhotoImage(file = "icons8-stop-48.png")
    its_VolumeIncrease = PhotoImage(file = "icons8-up-arrow-48.png")
    its_VolumeDecrease = PhotoImage(file = "icons8-scroll-down-48.png")
    its_Resume = PhotoImage(file = "icons8-play-64.png")
    its_Mute = PhotoImage(file = "icons8-mute-100.png") 
    its_UnMute = PhotoImage(file = "icons8-sound-64.png")


    #modify image size
    its_search = its_search.subsample(1,1)
    its_play = its_play.subsample(1,1)
    its_pause = its_pause.subsample(1,1)
    its_stop = its_stop.subsample(1,1)
    its_VolumeIncrease = its_VolumeIncrease.subsample(1,1)
    its_VolumeDecrease = its_VolumeDecrease.subsample(1,1)
    its_Resume = its_Resume.subsample(1,1)
    its_Mute = its_Mute.subsample(1,1)
    its_UnMute = its_UnMute.subsample(1,1)


    #creating labels
    AudioLabel = Label(root,text="Select Audio : ",background="Medium Orchid1",font=("Algerian",20))
    AudioLabel.grid(row=0,column=0,padx=20,pady=20)

    AudioStatusLabel = Label(root,text="",background="Medium Orchid1",font=("Comic Sans MS",20),width=10)
    AudioStatusLabel.grid(row=2,column=1)
    #creating entry box
    AudioLabelEntry = Entry(root,font = ("Comic Sans MS",20,"italic bold"),width=30,textvariable=AudioTrack)
    AudioLabelEntry.grid(row=0,column=1,padx=20,pady=20)
    #Buttons
    SearchButton = Button(root,text="SEARCH",bg="chartreuse2",font = ("Comic Sans MS",15,"italic bold"),width=200,bd=10,
                          activebackground="SpringGreen4",image=its_search,compound=RIGHT,command=MusicURL)
    SearchButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root,text="PLAY",bg="coral2",font = ("Comic Sans MS",15,"italic bold"),width=200,bd=10,
                          activebackground="coral4",image=its_play,compound=RIGHT,command=PlayMusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)

    root.PauseButton = Button(root,text="PAUSE",bg="DarkGoldenrod2",font = ("Comic Sans MS",15,"italic bold"),width=200,bd=10,
                          activebackground="DarkGoldenrod4",image=its_pause,compound=RIGHT,command=PauseMusic)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)
    


    root.ResumeButton = Button(root,text="RESUME",bg="DarkGoldenrod2",font = ("Comic Sans MS",15,"italic bold"),width=200,bd=10,
                          activebackground="DarkGoldenrod4",image=its_Resume,compound=RIGHT,command=ResumeMusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()

    root.MuteButton = Button(root,text="MUTE",width = 180,bg = "pale violet red",activebackground="light pink",bd=8,
                             font = ("Comic Sans MS",15,"italic bold"),image = its_Mute,compound=RIGHT,command=MuteMusic)
    root.MuteButton.grid(row=2,column=2)
    root.MuteButton.grid_remove()


    root.UnMuteButton = Button(root,text="UNMUTE",width = 180,bg = "pale violet red",activebackground="light pink",bd=8,
                               font = ("Comic Sans MS",15,"italic bold"),image = its_UnMute,compound=RIGHT,command=UnMuteMusic)
    root.UnMuteButton.grid(row=2,column=2)
    root.UnMuteButton.grid_remove()


    StopButton = Button(root,text="STOP",bg="brown4",font = ("Comic Sans MS",15,"italic bold"),width=200,bd=10,
                          activebackground="firebrick4",image=its_stop,compound=RIGHT,command=StopMusic)
    StopButton.grid(row=1,column=2,padx=20,pady=20)

    IncreaseVolumeButton = Button(root,text="VOLUME ",bg="PaleVioletRed1",font = ("Comic Sans MS",15,"italic bold"),width=200,bd=10,
                          activebackground="PaleVioletRed4",image=its_VolumeIncrease,compound=RIGHT,command=IncreaseVolume)
    IncreaseVolumeButton.grid(row=2,column=0,padx=20,pady=20)

    DecreaseVolumeButton = Button(root,text="VOLUME ",bg="gray69",font = ("Comic Sans MS",15,"italic bold"),width=200,bd=10,
                          activebackground="gray31",image=its_VolumeDecrease,compound=RIGHT,command=DecreaseVolume)
    DecreaseVolumeButton.grid(row=3,column=0,padx=20,pady=20)

    #ProgressbarLabel
    ProgressBarLabel = Label(root,text="",bg="dark green")
    ProgressBarLabel.grid(row=2,column=2,rowspan=5,padx=30,pady=30)
    ProgressBarLabel.grid_remove()

    ProgressBarVolume = Progressbar(ProgressBarLabel,orient=VERTICAL,mode="determinate",value=0,length=170)
    ProgressBarVolume.grid(row=0,column=0,ipadx=10)
    
    ProgressBarVolumeLevel = Label(ProgressBarLabel,text="0%",font = ("Comic Sans MS",9,"italic bold"),bg="thistle1",width=5)
    ProgressBarVolumeLevel.grid(row=0,column=0)
    
    #ProgressbarMusic
    ProgressBarMusicLabel = Label(root,text="",bg="burlywood3")
    ProgressBarMusicLabel.grid(row=5,column=0,columnspan=6,padx=20,pady=90)
    ProgressBarMusicLabel.grid_remove()

    ProgressBarMusicBegTimeLabel = Label(ProgressBarMusicLabel,text="0:00:0",bg="burlywood3",width=10)
    ProgressBarMusicBegTimeLabel.grid(row=5,column=0)

    ProgressBarMusic = Progressbar(ProgressBarMusicLabel,orient=HORIZONTAL,mode="determinate",value=0)
    ProgressBarMusic.grid(row=5,column=1,ipadx=400,ipady=5)
    

    ProgressBarMusicEndTimeLabel = Label(ProgressBarMusicLabel,text="0:00:0",bg="burlywood3")
    ProgressBarMusicEndTimeLabel.grid(row=5,column=2)

from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
root = Tk()
root.geometry("1060x650+150+40")
root.title("MUSIC PLAYER!!!")
root.iconbitmap("Music.ico")
root.resizable(False,False)
root.configure(bg="Medium Orchid1")
AudioTrack = StringVar()
CurrentVolume = 0
TotalSongLength=0
count=0
text=""
mixer.init()
CreateWidthes()
root.mainloop()


import time as t
import datetime as d
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as p

def validate(input_time):
    try:
        now = d.datetime.now()
        end_time = d.datetime.strptime(input_time,"%H:%M:%S").replace(year=now.year, month=now.month, day=now.day)
        if end_time < now:
            print("Invalid time. Please enter a time in the future.")
            return None
        else:
            return end_time
    except Exception:
        print("Invalid time format. Please enter HH:MM:SS.")
        return None    

def alarm(end_time):
    music = "C:/Users/ariro/Downloads/SpotifyMate.com - Grandmaster Hotel Lobby - Sohn Minsoo _DEVSISTERS_.mp3"
    print(f"Alarm set for {end_time.strftime("%H:%M:%S")}")
    print("********************************")
    while True:
        current_time = d.datetime.now()
        if current_time >= end_time:
            print("WAKE UP!!!!")
            p.mixer.init()
            p.mixer.music.load(music)
            p.mixer.music.play()
            while p.mixer.music.get_busy():
                t.sleep(1)
            break
        t.sleep(1)
        print(f"Current time : {current_time.strftime("%H:%M:%S")}")
        
            
        
        
print("********************************\nALARM\n********************************")
while True:
    input_time = input("\nEnter the time you want the alarm to go off (HH:MM:SS) : ")
    end_time = validate(input_time)
    if end_time:
        break
alarm(end_time)


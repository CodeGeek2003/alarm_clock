import datetime
import tkinter

import playsound
import time
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from threading import *

clock = Tk()
clock.geometry("450x250")

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        if current_time == set_alarm_time:
            print("Alarm Time")
            playsound.playsound("alarm.mp3")
            messagebox.showinfo("Alarm Clock", "Time to Wake up")
            break
lc=Label(clock, text="Alarm Clock", font=("Arial", 20, "bold"), fg="red",pady=20)
lc.pack(pady=10)
ls=Label(clock, text="Set Time", font=("Arial", 15, "bold"),pady=20)
ls.pack()

fm=Frame(clock)
fm.pack(pady=20)
hour=StringVar(clock)
hours=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24")
hours=OptionMenu(fm, hour, *hours)
hours.pack(side=LEFT)
minute=StringVar(clock)
minutes=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
minutes=OptionMenu(fm, minute, *minutes)
minutes.pack(side=LEFT)
second=StringVar(clock)
seconds=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
seconds=OptionMenu(fm, second, *seconds)
seconds.pack(side=LEFT)
Button(clock, text="Set Alarm", font=("Arial", 10, "bold"), command=Threading).place(x=180,y=200)
clock.mainloop()
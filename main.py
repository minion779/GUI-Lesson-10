from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.geometry("300x300")
root.title("Time Counter")

def timeCountdown():
    global temp
    try:
        temp = (int(hour.get())*3600) + (int(minute.get()) * 60) + (int(second.get()))
    except:
        print("Invalid Input")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("time", "Time Over!")
        temp = temp -1

hour = StringVar()
hour.set("00")

minute = StringVar()
minute.set("00")

second = StringVar()
second.set("00")

hourEntry = Entry(root, width = 3, font = ("Arial", 18, "bold"), textvariable = hour)
hourEntry.place(x = 80, y = 20)

minuteEntry = Entry(root, width = 3, font = ("Arial", 18, "bold"), textvariable = minute)
minuteEntry.place(x = 120, y = 20)

secondEntry = Entry(root, width = 3, font = ("Arial", 18, "bold"), textvariable = second)
secondEntry.place(x = 160, y = 20)

countdown = Button(root, text = "Set Time Countdown", command = timeCountdown)
countdown.place(x = 80, y = 70)

root.mainloop()
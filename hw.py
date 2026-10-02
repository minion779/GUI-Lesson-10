from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.geometry("300x300")
root.title("Kitchen Timer")
root.config(background = "lightblue")

def timeCountdown():
    global temp
    try:
        temp = (int(minute.get()) * 60) + (int(second.get()))
    except:
        print("Invalid Input")
    while temp > -1:
        mins, secs = divmod(temp, 60)

        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("time", "Time Over!")
        temp = temp -1

def sFEgg():
    global temp
    temp = 180
    # try:
    #     temp = (int(minute.get()) * 60) + (int(second.get()))
    # except:
    #     print("Invalid Input")
    while temp > -1:
        mins, secs = divmod(temp, 60)

        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("time", "Time Over!")
        temp = temp -1

def mBEgg():
    global temp
    temp = 300
    # try:
    #     temp = (int(minute.get()) * 60) + (int(second.get()))
    # except:
    #     print("Invalid Input")
    while temp > -1:
        mins, secs = divmod(temp, 60)

        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("time", "Time Over!")
        temp = temp -1

def hBEgg():
    global temp
    temp = 600
    # try:
    #     temp = (int(minute.get()) * 60) + (int(second.get()))
    # except:
    #     print("Invalid Input")
    while temp > -1:
        mins, secs = divmod(temp, 60)

        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("time", "Time Over!")
        temp = temp -1

minute = StringVar()
minute.set("00")

second = StringVar()
second.set("00")

minuteEntry = Entry(root, width = 3, font = ("Arial", 18, "bold"), textvariable = minute)
minuteEntry.place(x = 120, y = 20)

secondEntry = Entry(root, width = 3, font = ("Arial", 18, "bold"), textvariable = second)
secondEntry.place(x = 160, y = 20)

countdown = Button(root, text = "Set Time Countdown", command = timeCountdown)
countdown.place(x = 80, y = 70)

softBoiled = Button(root, text = "Soft Boiled Egg Time", command = sFEgg)
softBoiled.place(x = 80, y = 110)

mediumBoiled = Button(root, text = "Medium Boiled Egg Time", command = mBEgg)
mediumBoiled.place(x = 80, y = 150)

hardBoiled = Button(root, text = "Hard Boiled Egg Time", command = hBEgg)
hardBoiled.place(x = 80, y = 190)


root.mainloop()
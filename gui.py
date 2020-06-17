from tkinter import *

ps = Tk()

ps.attributes("-fullscreen", True)
ps.title('Forex-Sim')
ps.geometry("1366x768")

l4=Label(ps, text='FOREX TRAINER', font="Calibri 30 bold")
l4.pack(side=TOP, pady=(30,0))

windowframe = Frame(ps, width=1200, height=600, bg='black')
windowframe.pack(side = TOP , pady=(10,0))

ps.mainloop()

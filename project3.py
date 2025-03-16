from tkinter import Tk
from tkinter import Label
import time
root=Tk()
root.title("CLOCK")
def present_time():
    display_time=time.strftime("%H:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200,present_time)

digi_clock=Label(root,font=("sans-serif",100),bg="black",fg="yellow")
digi_clock.pack()
present_time()
root.mainloop()
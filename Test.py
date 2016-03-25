from tkinter import *

master = Tk()

w = Canvas(master, width=800, height=600)
w.pack()

w.create_arc(5,20,400,400,style=ARC, start=45, width=15)
#w.create_rectangle(50, 20, 150, 80, fill="#476042")
#w.create_rectangle(65, 35, 135, 65, fill="yellow")
#w.create_line(0, 0, 50, 20, fill="#476042", width=3)
#w.create_line(0, 100, 50, 80, fill="#476042", width=3)
#w.create_line(150,20, 200, 0, fill="#476042", width=3)
#w.create_line(150, 80, 200, 100, fill="#476042", width=3)

mainloop()
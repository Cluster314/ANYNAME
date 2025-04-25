from tkinter import *
w = Tk()
w.geometry("500x380")
w.config(cursor="plus")
def do(event):
    l.config(text=f"{event.x}, {event.y}")
img = PhotoImage(file="C:\\Users\\maasp\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-04-20 153552.png")
Label(w,image=img).pack()
l = Label(w,text="- - - -",font=("Arial",15))
l.pack()
w.bind("<Motion>",do)
w.mainloop()
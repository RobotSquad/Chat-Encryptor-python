from tkinter import Tk, Label
root=Tk()
def j():
    print("ver 2.1")
def key_pressed(event):
 if event.char == '+':
    j()
 w=Label(root,text="Key Pressed: "+event.char)
 w.place(x=70,y=90)
root.bind("<Key>",key_pressed)
root.mainloop()
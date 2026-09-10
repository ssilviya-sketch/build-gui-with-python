from tkinter import *
window = Tk()
window.title("Newsletter")
window.geometry('800x800')
b1 = Button(window,text = "play",background = "red",command = window.destroy)
b1.pack(side = 'top')
window.mainloop()

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def OpenFile():
    filepath = filedialog.askopenfilename()
    file = Image.open(filepath)
    file_new = file.resize((400, 400))
    render = ImageTk.PhotoImage(file_new)
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=0)

def TextLabel():
    entryBox = Entry()
    entryBox.pack()

window = Tk()
window.geometry("405x450")
button = Button(text='Open', command=OpenFile)
button.place(x=190, y=410)
TextLabel()
window.mainloop()

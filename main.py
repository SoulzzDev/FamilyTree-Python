from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def OpenFile():
    filepath = filedialog.askopenfilename()
    file = Image.open(filepath)
    render = ImageTk.PhotoImage(file)
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=0)


window = Tk()

button = Button(text='Open', command=OpenFile)
button.pack()
window.mainloop()

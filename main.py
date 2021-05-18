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


window = Tk()
window.geometry("400x400")

button = Button(text='Open', command=OpenFile)
button.pack()
window.mainloop()

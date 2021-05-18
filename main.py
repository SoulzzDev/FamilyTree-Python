from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

window = Tk()
window.geometry("405x450")

## File reader
def OpenFile():
    filepath = filedialog.askopenfilename()
    file = Image.open(filepath)
    file_new = file.resize((400, 400))
    render = ImageTk.PhotoImage(file_new)
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=0)

button = Button(text='Open', command=OpenFile)
button.place(x=190, y=410)
entryBox = Entry()
entryBox.pack()

## gets the text from the entrybox
def TextLabel():
    label = Label(text="entryBox.get()")
    label.pack()
    label.place(x=160, y=100)

textButton = Button(text="Enter", command=TextLabel())
textButton.pack()

window.mainloop()

from tkinter import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import *
from tkinter import filedialog
from PIL import Image, ImageTk


class filedialog:
    window = Tk()
    window.geometry("405x450")

    ## File reader
    def OpenFile(self):
        filepath = QFileDialog.getOpenFileName(self, 'Open File')
        print(filepath)
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

    window.mainloop()


filedialog()
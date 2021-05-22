from tkinter import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from tkinter import filedialog
from PyQt5.QtCore import *
from PIL import Image, ImageTk


class app(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Reader")
        self.setGeometry(100, 100, 600, 400)
        self.InitUI()
        self.show()


    def InitUI(self):
        button = QPushButton('moi', self)
        button.move(100, 70)
        button.clicked.connect(self.OpenFile)

    ## File reader
    def OpenFile(self):
        filepath = QFileDialog.getOpenFileName(None, "Open file", "All Files","Image files (*.jpg *.png")
        print(filepath)
        file = Image.open(filepath)
        file_new = file.resize((400, 400))
        render = ImageTk.PhotoImage(file_new)
        img = Label(image=render)
        img.image = render
        img.place(x=0, y=0)


App = QApplication(sys.argv)
window = app()
sys.exit(App.exec())

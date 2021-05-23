from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit, QLineEdit
import sys
from PyQt5.QtCore import *

from PyQt5.QtGui import QPixmap


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Kuori OY"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.InitUI()

    def InitUI(self):
        self.setWindowIcon(QtGui.QIcon("kuori_logo.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.textLine = QLineEdit()
        self.textLine.editingFinished.connect(self.enterPressed)
        vbox.addWidget(self.textLine)

        self.label = QLabel()
        vbox.addWidget(self.label)

        self.btn1 = QPushButton("Open Image")
        self.btn1.clicked.connect(self.openFile)
        vbox.addWidget(self.btn1)

        self.setLayout(vbox)

        self.show()


    def enterPressed(self):
        self.label.setText(self.textLine.text())

    def openFile(self):
        filepath = QFileDialog.getOpenFileName()
        imagePath = filepath[0]
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaled(250, 350, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
#        self.resize(pixmap.width(), pixmap.height())


app = QApplication(sys.argv)
window = App()
sys.exit(app.exec())

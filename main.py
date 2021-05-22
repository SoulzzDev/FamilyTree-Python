from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit
import sys

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

        self.btn1 = QPushButton("Open Image")
        self.btn1.clicked.connect(self.openFile)

        vbox.addWidget(self.btn1)

        self.label = QLabel("Image position")
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def openFile(self):
        filepath = QFileDialog.getOpenFileName(None, "Open file", "All Files","Image files (*.jpg *.png")
        imagePath = filepath[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())

app = QApplication(sys.argv)
window = App()
sys.exit(app.exec())

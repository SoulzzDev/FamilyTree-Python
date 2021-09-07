from PyQt5.QtWidgets import *

from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Kuori OY"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.UI()

    def UI(self):
#        self.setWindowIcon(QtGui.QIcon("kuori_logo.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.vbox = QVBoxLayout()

        self.setLayout(self.vbox)

        self.showFullScreen()

stylesheet = """
    MainWindow {
        background-image: url("D:/blender kamat/JarkonLatexMenu3");
        background-repeat: no-repeat;
        background-position: center;
    }
"""

import sys
app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window = MainWindow()
sys.exit(app.exec())

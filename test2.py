from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self, text, image, color):
        QWidget.__init__(self)

        self.setMinimumSize(100, 100)
        self.img = image
        self.setStyleSheet("height: auto;background-color: " + color + " ;border-image:url(" + self.img + "); ")

        self.label = QLabel(self)
        self.label.setText(text)
        self.label.setStyleSheet("font: 18pt; color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def set_text(self, text):
        # modifier le texte
        self.label.setText(text)

    def set_color(self, color):
        # change la couleur
        self.setStyleSheet("height: auto;background-color: %s ;" + "border-image:url(%s);" % color % self.img)


if __name__ == '__main__':
    MainEvntHndlr = QApplication([])

    MainApp = MyWidget("Hello", "Mountains.jpg", "green")
    MainApp.show()

    MainEvntHndlr.exec()
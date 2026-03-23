import sys
from PySide6 import QtCore, QtWidgets, QtGui

#please just work now
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.input = QtWidgets.QLineEdit()
        self.input.setPlaceholderText("random text")
        self.button = QtWidgets.QPushButton("Push Button to append text")
        self.text = QtWidgets.QTextEdit()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.append(self.input.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
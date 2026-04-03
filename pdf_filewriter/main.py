import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QTextEdit


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.input = QtWidgets.QLineEdit()
        self.input.setPlaceholderText("random text")
        
        self.button = QtWidgets.QPushButton("Push Button to append text")
        self.text = QtWidgets.QTextEdit()
        
        self.stack = QtWidgets.QStackedLayout()
        
        # Import Page
        importPage = QtWidgets.QWidget()
        importPageLayout = QtWidgets.QVBoxLayout(importPage)
        importPageLayout.addWidget(self.input)
        importPageLayout.addWidget(self.button)
        importPageLayout.addWidget(self.text)
        
        # Config Page
        configPage = QtWidgets.QWidget()
        configPageLayout = QtWidgets.QVBoxLayout(configPage)
        configPageLayout.addWidget(QtWidgets.QLabel("Config Area"))
        
        self.stack.addWidget(importPage)
        self.stack.addWidget(configPage)
        
        self.setLayout(self.stack)
        
        self.button.clicked.connect(lambda: self.stack.setCurrentIndex(1))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = MyWidget()
    widget.setWindowTitle("PDF-Filewriter")
    widget.resize(800, 600)
    widget.show()
    
    sys.exit(app.exec())

import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QTextEdit


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # All the elements
        importButton = QtWidgets.QPushButton("Import")
        
        self.stack = QtWidgets.QStackedLayout()
        
        # Import Page
        importPage = QtWidgets.QWidget()
        importPageLayout = QtWidgets.QVBoxLayout(importPage)
        importPageLayout.addWidget(importButton)
        
        # Config Page
        configPage = QtWidgets.QWidget()
        configPageLayout = QtWidgets.QVBoxLayout(configPage)
        
        self.stack.addWidget(importPage)
        self.stack.addWidget(configPage)
        
        self.setLayout(self.stack)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = MyWidget()
    widget.setWindowTitle("PDF-Filewriter")
    widget.resize(800, 600)
    widget.show()
    
    sys.exit(app.exec())

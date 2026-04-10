import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QTextEdit
from markdown_it import MarkdownIt


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # All the elements
        self.importButton = QtWidgets.QPushButton("Import")
        self.importButton.clicked.connect(self.loadFile)
        
        self.stack = QtWidgets.QStackedLayout()
        
        # Import Page
        self.importPage = QtWidgets.QWidget()
        self.importPageLayout = QtWidgets.QVBoxLayout(self.importPage)
        self.importPageLayout.addWidget(self.importButton)
        
        # Config Page
        self.configPage = QtWidgets.QWidget()
        self.configPageLayout = QtWidgets.QVBoxLayout(self.configPage)
        self.fileDisplay = QtWidgets.QTextBrowser(self.configPage)
        #self.fileDisplay.setWordWrap(True)
        self.configPageLayout.addWidget(self.fileDisplay)
        
        self.stack.addWidget(self.importPage)
        self.stack.addWidget(self.configPage)
        
        self.setLayout(self.stack)
    
    def loadFile(self):
        # Open a File dialog when the button is pressed
        
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        print("File Path: " + self.fname)

        with open (self.fname, 'r') as f:
            self.content = f.read()

        md = MarkdownIt()
        html = md.render(self.content)

        self.fileDisplay.setText(html)

        self.stack.setCurrentIndex(1)

        #self.safeFile()

    #def safeFile(self):
    #    with open(self.fname, 'r') as f:
    #        self.content = f.read()
    #    self.stack.setCurrentIndex(1)
    #    self.fileDisplay.setText(self.content)


    # Dragging and Dropping Files for the app
    def dragEnterEvent(self, e):
        if e.mimeDat().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMovementEvent(self, e):
        if e.mimeDat().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls:
            e.setDropAction(QtWidgets.Qt.CopyAction)
            e.accept()

            self.fname = fname
            #self.safeFile()
        else:
            e.ignore()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = MyWidget()
    widget.setWindowTitle("PDF-Filewriter")
    widget.resize(800, 600)
    widget.show()
    
    sys.exit(app.exec())

from PyQt5.Qt import *
from PyQt5.uic import loadUi
import sys
import os


class maingui(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui()

    def gui(self):
        loadUi('maingui.ui', self)
        self.bFile.clicked.connect(self.loadFile)
        self.show()

    def loadFile(self):
        '''loads some files to the GUI'''

        a = QFileDialog()
        f = a.getOpenFileNames(self, 'Open a file!', filter='All image files (*.png *.jpg *.wav);;All sound files (*.mp3 *.aac)')
        for item in f[0]:
            self.text.appendPlainText(item)
            nFiles=len(f[0])
        self.lblFileCount.setText(str(nFiles))
        self.statusBar().showMessage('Opened {} files'.format(nFiles), 2000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m=maingui()
    sys.exit(app.exec_())

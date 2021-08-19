import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog


class limp4FS():
    def openFileDialogEvent(self):
        fname=QFileDialog.getOpenFileNames(self, 'Select Video', "./", "Video Or Audio files (*.mp3 *.mp4 *.wav *.mov)")

"""
.app.py
DOCUMENTATION
LICENSE: ALL RIGHTS RESERVED

Tutorial based on:
Create a Python Audio App with PyQt – Fast & Easy GUI Development
https://www.youtube.com/watch?v=wdEpWCFf40U&list=PL-Ng7SwSuj9Oj3EzaC38Zm90oo75E9V1f&index=12&t=30s
"""

import os
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QListWidget,
    QFileDialog,
    QSlider,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt, QTimer, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


# MyApp
# Run as a class
class AudioApp(QWidget):  # Every widget we see is a QWidget
    def __init__(self):
        super().__init__()  # Activate the QWidget Superclass
        self.settings()

    # Settings
    def settings(self):
        self.setWindowTitle("Audio Adjuster")
        self.setGeometry(240, 210, 600, 300)

    # Design


    # Event Handler

if __name__ == "__main__":
    app = QApplication([])
    main = AudioApp()
    main.show()
    app.exec()

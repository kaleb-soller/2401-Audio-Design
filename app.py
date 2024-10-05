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
        self.initUI()

    # Settings
    def settings(self):
        self.setWindowTitle("Audio Player")
        self.setGeometry(240, 210, 600, 300)

    # Design
    def initUI(self):
        self.title = QLabel("Volume Slider")
        self.file_list = QListWidget()
        self.btn_opener = QPushButton("Choose a file")
        self.btn_play = QPushButton("Play")
        self.btn_pause = QPushButton("Pause")
        self.btn_resume = QPushButton("Resume")
        self.btn_reset = QPushButton("Reset")

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(50)
        self.slider.setMaximum(150)
        self.slider.setValue(100)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)

        # Create a layout
        # Master (Columns or rows, or just the objects)
        self.master = QVBoxLayout()
        row = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        self.master.addWidget(self.title)
        self.master.addWidget(self.slider)

        col1.addWidget(self.file_list)
        col2.addWidget(self.btn_opener)
        col2.addWidget(self.btn_play)
        col2.addWidget(self.btn_pause)
        col2.addWidget(self.btn_resume)
        col2.addWidget(self.btn_reset)

        row.addLayout(col1)
        row.addLayout(col2)

        self.master.addLayout(row)

        self.setLayout(self.master)

    # Event Handler


if __name__ == "__main__":
    app = QApplication([])
    main = AudioApp()
    main.show()
    app.exec()

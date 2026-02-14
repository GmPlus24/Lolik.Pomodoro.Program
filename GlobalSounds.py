from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QToolButton, QMessageBox, QDialog, QSystemTrayIcon, QMenu, QSpinBox, QComboBox, QCheckBox, QSplashScreen, QStatusBar
from PyQt6.QtGui import QFont, QIcon, QColor, QAction, QPixmap
from PyQt6.QtCore import QSize, QTimer, Qt, QUrl, QSettings, QEvent, QUrl
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6 import QtGui
from PyQt6 import QtWidgets
import time
from time import strftime
from datetime import datetime, timedelta
import sys
import ctypes



def mySounds(self):
    # sound
    self.effect1 = QSoundEffect(self)
    self.effect1.setSource(QUrl.fromLocalFile("Sounds\Ring-sound-effect.wav"))
    self.effect1.setLoopCount(5)
    self.effect1.setVolume(0.75)
    
    self.effect2 = QSoundEffect(self)
    self.effect2.setSource(QUrl.fromLocalFile("Sounds\Ring-sound-effect.wav"))
    self.effect2.setLoopCount(5)
    self.effect2.setVolume(0.75)
    
    self.effect3 = QSoundEffect(self)
    self.effect3.setSource(QUrl.fromLocalFile("Sounds\Ring-sound-effect.wav"))
    self.effect3.setLoopCount(5)
    self.effect3.setVolume(0.75)
    
    # user test sound
    self.userTestEffect = QSoundEffect(self)
    self.userTestEffect.setLoopCount(1)
    self.userTestEffect.setVolume(0.75)
    
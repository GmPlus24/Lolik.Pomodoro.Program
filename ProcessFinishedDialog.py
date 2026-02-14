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


def ProcessFinishedDialog(self):
    self.ProcessFinishedDialog = QDialog(self)
    self.ProcessFinishedDialog.setWindowTitle("Good Job!")
    self.ProcessFinishedDialog.setWindowIcon(QIcon("Icons\information-icon.png"))
    self.ProcessFinishedDialog.resize(500,300)
    self.setFixedWidth(500)
    self.setFixedHeight(300)
    
    self.myIcon = QLabel(self.ProcessFinishedDialog)
    self.myIcon.setPixmap(QPixmap("Icons\Lolik-MainIcon-Small.png"))
    self.myIcon.move(15,30)
    
    self.myText = QLabel(self.ProcessFinishedDialog)
    self.myText.move(250,15)
    self.myText.setText("\n\nYou work 3 times! Take a long break,\n click the long break button.")
    
    self.myTextInfo = QLabel(self.ProcessFinishedDialog)
    self.myTextInfo.move(250,107)
    self.myTextInfo.setStyleSheet("color: blue")
    self.myTextInfo.resize(200,34)
    self.myTextInfo.setText("You can break: " + self.long_break_spinbox.text() + "\n" + "Get back to work: " + str(( datetime.now() + timedelta(minutes =  int(self.long_break_spinbox.value())  )).strftime('%H:%M')))
    
    self.myTextInfo2 = QLabel(self.ProcessFinishedDialog)
    self.myTextInfo2.move(250,179)
    self.myTextInfo2.setText("Closing message box after:")
    
    self.myTextInfo3 = QLabel(self.ProcessFinishedDialog)
    self.myTextInfo3.move(250,187)
    self.myTextInfo3.setStyleSheet("color:red")
    font = self.myTextInfo3.font()
    font.setPointSize(30)
    font.setBold(True)
    self.myTextInfo3.setFont(font)
    self.myTextInfo3.setText("20")
    
    self.myOkButton = QPushButton(self.ProcessFinishedDialog)
    self.myOkButton.setText("OK")
    self.myOkButton.resize(80,30)
    self.myOkButton.move(413, 265)
    self.myOkButton.clicked.connect(self.myDialogOk)
    

    
def DialogTimerCallBack(self):
    if self.var_countdown_timer > 0:
        self.var_countdown_timer -= 1

    if self.var_countdown_timer == 0:
        self.TimerDiloag.stop()


    minutes, seconds = divmod(self.var_countdown_timer, 60)
    self.sec_var = (f"{seconds:02d}")
    self.myTextInfo3.setText(self.sec_var)


def StartDialogTimer(self):
    # start 30 minute timer
    self.var_countdown_timer = self.time_seconds
    self.TimerDiloag.start()
    
    
def myDialogOk(self):
    self.ProcessFinishedDialog.close()
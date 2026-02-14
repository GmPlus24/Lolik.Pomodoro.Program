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


def myVariables(self):
    self.program_name = "Lolik"

    #Variables
    self.min_var = 0
    self.sec_var = 0
    self.count_work = 0
    self.count_work_user = 0
    self.time_seconds = 20
    self.time_milliseconds = self.time_seconds * 1000
    
    self.start_sound = 2
    self.break_sound = 4
    self.long_break_sound = 3
    self.times_for_repeat = 5
    self.message_box_check = "CHECK"
    
    self.process_mode = "SINGLE SHOT"
    
    self.debug = 0
    
    self.alarmVar = 0
    
    self.flagCollapseExpandWindow = 0
    self.flagLabelCollapse = 0
    self.flagMuteUnmuteSound = 0
    
    self.labelFont = "NORMAL"
    self.windowCollapseModeFlag = "TOP"
    self.windowCollapseModeFontSize = 60
    
    self.workIsStarted = 0
    self.breakIsStarted = 0
    self.longBreakIsStarted = 0
    
    self.pauseResumeValue = 0

    
    

    self.Timer25min = QTimer(self) #main timer
    self.Timer25min.setInterval(1000)
    self.Timer25min.timeout.connect(self.start_work_TimerCallBack)
    
    self.Timer5min = QTimer(self) #main timer
    self.Timer5min.setInterval(1000)
    self.Timer5min.timeout.connect(self.start_break_TimerCallBack)
    
    self.Timer30min = QTimer(self) #main timer
    self.Timer30min.setInterval(1000)
    self.Timer30min.timeout.connect(self.start_long_break_TimerCallBack)
    
    self.TimerDiloag = QTimer(self)
    self.TimerDiloag.setInterval(1000)
    self.TimerDiloag.timeout.connect(self.DialogTimerCallBack)
    
    self.TimerTestSound = QTimer(self)
    self.TimerTestSound.setInterval(100)
    self.TimerTestSound.timeout.connect(self.disableStopButton)
    
    self.TimerAlarmNotification = QTimer(self)
    self.TimerAlarmNotification.setInterval(500)
    self.TimerAlarmNotification.timeout.connect(self.alarmNotificationTimerCallBack)
    
    pass
    
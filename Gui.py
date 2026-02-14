from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QToolButton, QMessageBox, QDialog, QSystemTrayIcon, QMenu, QSpinBox, QComboBox, QCheckBox, QSplashScreen, QStatusBar, QProgressBar, QFrame, QLCDNumber
from PyQt6.QtGui import QFont, QIcon, QColor, QAction, QPixmap
from PyQt6.QtCore import QSize, QTimer, Qt, QUrl, QSettings, QEvent, QUrl, pyqtSignal
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6 import QtGui
from PyQt6 import QtWidgets
import time
from time import strftime
from datetime import datetime, timedelta
import sys
import ctypes



class myQLabel(QLabel):
    clicked=pyqtSignal()
    def mousePressEvent(self, ev):
        self.clicked.emit()
        
class myLCDNumber(QLCDNumber):
    clicked=pyqtSignal()
    def mousePressEvent(self, ev):
        self.clicked.emit()


def myGui(self):
    # min lcd number
    self.min_lcd_number = myLCDNumber(self)
    self.min_lcd_number.display("25")
    self.min_lcd_number.setDigitCount(2)
    self.min_lcd_number.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
    self.min_lcd_number.setStyleSheet("QLCDNumber{color:rgb(0, 0, 0);background-color:rgb(255, 255, 255); border: 0px solid blue;}")
    self.min_lcd_number.move(160,10)
    self.min_lcd_number.setFixedSize(60, 50)
    
    
    
    # sec lcd number
    self.sec_lcd_number = myLCDNumber(self)
    self.sec_lcd_number.display("00")
    self.sec_lcd_number.setDigitCount(2)
    self.sec_lcd_number.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
    self.sec_lcd_number.setStyleSheet("QLCDNumber{color:rgb(0, 0, 0);background-color:rgb(255, 255, 255); border: 0px solid blue;}")
    self.sec_lcd_number.move(235, 10)
    self.sec_lcd_number.setFixedSize(60, 50)
    
    

    # min label
    self.min_label = myQLabel("25", self)
    self.min_label.setFont(QFont("Sansserif", 40, QFont.Weight.Bold))
    self.min_label.setStyleSheet("background-color:white;")
    self.min_label.move(148,10)
    self.min_label.setFixedSize(70, 50)
    
    # sec label
    self.sec_label = myQLabel("00", self)
    self.sec_label.setFont(QFont("Sansserif", 40, QFont.Weight.Bold))
    self.sec_label.setStyleSheet("background-color:white;")
    self.sec_label.move(237, 10)
    self.sec_label.setFixedSize(70, 50)
    
    self.min_label.hide()
    self.sec_label.hide()
    
    # : label
    self.label1 = myQLabel(":", self)
    self.label1.setFont(QFont("Sansserif", 40, QFont.Weight.Bold))
    self.label1.setStyleSheet("background-color:white")
    self.label1.move(218, 10)
    self.label1.setFixedSize(19, 50)
    
    # system time label
    self.system_time_label = myQLabel("System Time:", self)
    self.system_time_label.setFont(QFont("Sansserif", 11))
    self.system_time_label.setStyleSheet("background-color:gray; color:white;")
    self.system_time_label.move(157, 70)
    self.system_time_label.setFixedSize(143, 38)
    self.system_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    # system time label in collapse mode
    self.system_time_label_2 = myQLabel(self)
    self.system_time_label_2.setFont(QFont("Sansserif", 34, QFont.Weight.Bold))
    self.system_time_label_2.setStyleSheet("background-color:white; color:black;")
    self.system_time_label_2.move(157, 70)
    self.system_time_label_2.setFixedSize(143, 38)
    self.system_time_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.system_time_label_2.hide()
    
    # process combo box
    self.process_combobox = QComboBox(self)
    self.process_combobox.setToolTip("Set Process")
    self.process_combobox.addItem("Auto - Continuous")
    self.process_combobox.addItem("Single Shot")
    self.process_combobox.setFixedSize(143, 23)
    self.process_combobox.move(157, 119)
    
    
    # progress bar
    self.myProgressBar = QProgressBar(self)
    self.myProgressBar.setMaximum(100)
    self.myProgressBar.setValue(0)
    self.myProgressBar.move(10,10)
    #self.myStatusBar.setStyleSheet(" QProgressBar { border: 2px solid grey; border-radius: 0px; text-align: center; } QProgressBar::chunk {background-color: #3add36; width: 1px;}")
    self.myProgressBar.setStyleSheet(" QProgressBar  {  border-radius: 5px; text-align: center; } QProgressBar::chunk {background-color: #3add36; width: 1px;}")
    self.myProgressBar.setFormat('')
    
    # alarm notification
    self.myAlarmNotification = QLabel(self)
    self.myAlarmNotification.setToolTip("Alarm Notification")
    self.myAlarmNotification.setPixmap(QPixmap("Icons\icons8-notification-bell-24.png"))
    self.myAlarmNotification.hide()
    
    # status bar
    self.myStatusBar = QStatusBar(self)
    self.myStatusBar.showMessage("Ready")
    font = self.myStatusBar.font()
    font.setBold(True)
    self.myStatusBar.setFont(font)
    self.myStatusBar.setStyleSheet("color: red")
    self.setStatusBar(self.myStatusBar)
    self.myStatusBar.addPermanentWidget(self.myProgressBar)
    self.myStatusBar.addPermanentWidget(self.myAlarmNotification)
    self.myStatusBar.setToolTip("At the end of 'work timer', Loop counts.")    
    
    # buttons
    self.btn_start = QPushButton("Start", self)
    self.btn_start.setToolTip("Start Work")
    self.btn_start.setStyleSheet('background-color:rgb(63, 186, 41);')
    self.btn_start.move(38, 207)
    self.btn_start.setFixedSize(90, 30)
    
    self.btn_break = QPushButton("Break", self)
    self.btn_break.setToolTip("Have a Break")
    self.btn_break.setStyleSheet('background-color:rgb();')
    self.btn_break.move(134, 207)
    self.btn_break.setFixedSize(90, 30)
    
    self.btn_long_break = QPushButton("Long Break", self)
    self.btn_long_break.setToolTip("Have a Long Break")
    self.btn_long_break.setStyleSheet('background-color:rgb();')
    self.btn_long_break.move(231, 207)
    self.btn_long_break.setFixedSize(90, 30)
    
    self.btn_cancel = QPushButton("Cancel", self)
    self.btn_cancel.setToolTip("Cancel the Process")
    self.btn_cancel.setEnabled(False)
    self.btn_cancel.setStyleSheet('background-color:rgb();')
    self.btn_cancel.move(324, 207)
    self.btn_cancel.setFixedSize(90, 30)
   
    
    
    # settings
    self.work_spinbox = QSpinBox(self)
    self.work_spinbox.setValue(25)
    self.work_spinbox.setRange(1, 99)
    self.work_spinbox.setSuffix(" m")
    self.work_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.work_spinbox.setToolTip("Set Your Work Time (minute)")
    self.work_spinbox.setFixedSize(90, 26)
    self.work_spinbox.move(38, 241)
    
    self.break_spinbox = QSpinBox(self)
    self.break_spinbox.setValue(5)
    self.break_spinbox.setRange(1, 99)
    self.break_spinbox.setSuffix(" m")
    self.break_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.break_spinbox.setToolTip("Set Your Break Time (minute)")
    self.break_spinbox.setFixedSize(90, 26)
    self.break_spinbox.move(134, 241)
    
    self.long_break_spinbox = QSpinBox(self)
    self.long_break_spinbox.setValue(30)
    self.long_break_spinbox.setRange(1, 99)
    self.long_break_spinbox.setSuffix(" m")
    self.long_break_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.long_break_spinbox.setToolTip("Set Your Long Break Time (minute)")
    self.long_break_spinbox.setFixedSize(90, 26)
    self.long_break_spinbox.move(231, 241)
    
    self.btn_reset = QPushButton("Times Reset", self)
    self.btn_reset.setToolTip("Times Reset")
    self.btn_reset.move(324, 239)
    self.btn_reset.setFixedSize(90, 30)
    
    
    
    
    self.btn_info = QPushButton(self)
    self.btn_info.setFlat(True)
#    self.btn_info.setToolTip("About " + main.program_name)
    self.btn_info.setIcon(QIcon('Icons\information-icon.png'))
    self.btn_info.setIconSize(QSize(24, 24))
    self.btn_info.setFixedSize(30, 30)
    self.btn_info.move(417,5)
    
    self.btn_qt_info = QPushButton(self)
    self.btn_qt_info.setFlat(True)
    self.btn_qt_info.setToolTip("About Qt")
    self.btn_qt_info.setIcon(QIcon('Icons\qt-icon.png'))
    self.btn_qt_info.setIconSize(QSize(24, 24))
    self.btn_qt_info.setFixedSize(30, 30)
    self.btn_qt_info.move(417, 35)
    
    '''
    self.btn_quit = QPushButton(self)
    self.btn_quit.setFlat(True)
    self.btn_quit.setToolTip("Quit")
    self.btn_quit.setIcon(QIcon('Icons\quit-icon.png'))
    self.btn_quit.setIconSize(QSize(24, 24))
    self.btn_quit.setFixedSize(30, 30)
    self.btn_quit.move(387, 65)
    self.btn_quit.clicked.connect(main._quit)
    '''
    
    self.myHorisontalLine = QLabel("_____", self)
    self.myHorisontalLine.setFixedSize(30, 30)
    self.myHorisontalLine.move(419, 48)
    
    self.btn_clock = QPushButton(self)
    self.btn_clock.setFlat(True)
    self.btn_clock.setToolTip("Settings")
    self.btn_clock.setIcon(QIcon('Icons\settings-icon.png'))
    self.btn_clock.setIconSize(QSize(24, 24))
    self.btn_clock.setFixedSize(30, 30)
    self.btn_clock.move(417, 75)
    
    self.btn_pause_play = QPushButton(self)
    self.btn_pause_play.setEnabled(False)
    self.btn_pause_play.setFlat(True)
    self.btn_pause_play.setToolTip("Pause/Play")
    self.btn_pause_play.setIcon(QIcon('Icons\icons8-pause-48.png'))
    self.btn_pause_play.setIconSize(QSize(48, 48))
    self.btn_pause_play.setFixedSize(30, 30)
    self.btn_pause_play.move(70, 170)
    
    self.btn_mute_unmute = QPushButton(self)
    self.btn_mute_unmute.setFlat(True)
    self.btn_mute_unmute.setToolTip("Mute/Unmute")
    self.btn_mute_unmute.setIcon(QIcon('Icons\icons8-sound-48.png'))
    self.btn_mute_unmute.setIconSize(QSize(32, 32))
    self.btn_mute_unmute.setFixedSize(30, 30)
    self.btn_mute_unmute.move(170, 170)
    
    self.btn_collapse_expand = QPushButton(self)
    self.btn_collapse_expand.setFlat(True)
    self.btn_collapse_expand.setToolTip("Collapse/Expand Window")
    self.btn_collapse_expand.setIcon(QIcon('Icons\collapse-icon.png'))
    self.btn_collapse_expand.setIconSize(QSize(32, 32))
    self.btn_collapse_expand.setFixedSize(30, 30)
    self.btn_collapse_expand.move(262, 170)
    

    
    pass
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





def collapseExpandeWindow(self):
    if self.flagCollapseExpandWindow == 0:
        # set flag value
        self.flagCollapseExpandWindow = 1
        
        # set window geometry
        self.resize(100,40)
        self.setFixedWidth(248)
        self.setFixedHeight(140)
        
        if self.dialog_checkbox_stay_on_top.isChecked():
            self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
            self.showNormal()
        if not self.dialog_checkbox_stay_on_top.isChecked():
            self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)
            self.showNormal()
        
        # set times label font, size, position
        self.min_label.setFont(QFont("Sansserif", 60, QFont.Weight.Bold))
        self.sec_label.setFont(QFont("Sansserif", 60, QFont.Weight.Bold))
        self.label1.setFont(QFont("Sansserif", 60, QFont.Weight.Bold))
        self.min_label.setFixedSize(100, 70)
        self.sec_label.setFixedSize(100, 70)
        self.label1.setFixedSize(28, 70)
        self.min_label.move(10,10)
        self.sec_label.move(138, 10)
        self.label1.move(110, 10)
        
        self.min_lcd_number.setFixedSize(100, 70)
        self.sec_lcd_number.setFixedSize(100, 70)
        self.min_lcd_number.move(15,10)
        self.sec_lcd_number.move(138, 10)
        
        
        self.system_time_label.hide()
        self.system_time_label_2.hide()
        self.process_combobox.hide()
       
        self.myProgressBar.hide()
        self.myAlarmNotification.hide()
        self.myStatusBar.hide()

        
        self.btn_start.setText("")
        self.btn_start.setToolTip("Start Work")
        self.btn_start.setIcon(QIcon('Icons\start-icon.png'))
        self.btn_start.setIconSize(QSize(20,20))
        self.btn_start.setFlat(True)
        self.btn_start.move(27, 100)
        self.btn_start.setFixedSize(20, 20)
        
        self.btn_break.setText("")
        self.btn_break.setToolTip("Have a Break")
        self.btn_break.setIcon(QIcon('Icons\icons8-break-48.png'))
        self.btn_break.setIconSize(QSize(20,20))
        self.btn_break.setFlat(True)
        self.btn_break.move(57, 100)
        self.btn_break.setFixedSize(20, 20)
        
        self.btn_long_break.setText("")
        self.btn_long_break.setToolTip("Have a Long Break")
        self.btn_long_break.setIcon(QIcon('Icons\long-break-icon.png'))
        self.btn_long_break.setIconSize(QSize(20,20))
        self.btn_long_break.setFlat(True)
        self.btn_long_break.move(87, 100)
        self.btn_long_break.setFixedSize(20, 20)
        
        self.btn_cancel.setText("")
        self.btn_cancel.setToolTip("Cancel the Process")
        self.btn_cancel.setIcon(QIcon('Icons\cancel-icon.png'))
        self.btn_cancel.setIconSize(QSize(20,20))
        self.btn_cancel.setFlat(True)
        self.btn_cancel.move(115, 100)
        self.btn_cancel.setFixedSize(20, 20)
        
        self.btn_pause_play.setText("")
        self.btn_pause_play.setToolTip("Pause/Play")
        self.btn_pause_play.setIconSize(QSize(30, 30))
        self.btn_pause_play.setFlat(True)
        self.btn_pause_play.move(140, 100)
        self.btn_pause_play.setFixedSize(20, 20)
        
        self.btn_mute_unmute.setText("")
        self.btn_mute_unmute.setToolTip("Mute/Unmute")
        self.btn_mute_unmute.setIconSize(QSize(20, 20))
        self.btn_mute_unmute.setFlat(True)
        self.btn_mute_unmute.move(167, 100)
        self.btn_mute_unmute.setFixedSize(20, 20)
        
        self.btn_collapse_expand.setText("")
        self.btn_collapse_expand.setToolTip("Collapse/Expand Window")
        self.btn_collapse_expand.setIcon(QIcon('Icons\expand-icon.png'))
        self.btn_collapse_expand.setIconSize(QSize(20, 20))
        self.btn_collapse_expand.setFlat(True)
        self.btn_collapse_expand.move(192, 100)
        self.btn_collapse_expand.setFixedSize(20, 20)
        
       
        self.work_spinbox.hide()
        self.break_spinbox.hide()
        self.long_break_spinbox.hide()
        self.btn_reset.hide()    
        
        self.btn_info.hide()
        self.btn_qt_info.hide()
    #    self.btn_quit.hide()
        self.btn_clock.hide()
    




    # ---------- expand window ----------
    else:
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)
        self.showNormal()
        
        self.flagCollapseExpandWindow = 0
        self.setFixedWidth(451)
        self.setFixedHeight(315)
        self.min_label.setFont(QFont("Sansserif", 40, QFont.Weight.Bold))
        self.sec_label.setFont(QFont("Sansserif", 40, QFont.Weight.Bold))
        self.label1.setFont(QFont("Sansserif", 40, QFont.Weight.Bold))
        self.min_label.setFixedSize(70, 50)
        self.sec_label.setFixedSize(70, 50)
        self.label1.setFixedSize(19, 50)
        self.min_label.move(148,10)
        self.sec_label.move(237, 10)
        self.label1.move(218, 10)
        
        self.min_lcd_number.setFixedSize(60, 50)
        self.sec_lcd_number.setFixedSize(60, 50)
        self.min_lcd_number.move(160,10)
        self.sec_lcd_number.move(235, 10)
        
        
        self.system_time_label.show()
        self.system_time_label_2.hide()
        self.process_combobox.show()
       
        self.myProgressBar.show()
        self.myAlarmNotification.hide()
        self.myStatusBar.show()
        
        
        
        self.btn_start.setText("Start")
        self.btn_start.setToolTip("Start Work")
        self.btn_start.setIcon(QIcon())
        self.btn_start.setIconSize(QSize(20,20))
        self.btn_start.setFlat(False)
        self.btn_start.move(38, 207)
        self.btn_start.setFixedSize(90, 30)
        
        self.btn_break.setText("Break")
        self.btn_break.setToolTip("Have a Break")
        self.btn_break.setIcon(QIcon())
        self.btn_break.setIconSize(QSize(20,20))
        self.btn_break.setFlat(False)
        self.btn_break.move(134, 207)
        self.btn_break.setFixedSize(90, 30)
        
        self.btn_long_break.setText("Long Break")
        self.btn_long_break.setToolTip("Have a Long Break")
        self.btn_long_break.setIcon(QIcon())
        self.btn_long_break.setIconSize(QSize(20,20))
        self.btn_long_break.setFlat(False)
        self.btn_long_break.move(231, 207)
        self.btn_long_break.setFixedSize(90, 30)
        
        self.btn_cancel.setText("Cancel")
        self.btn_cancel.setToolTip("Cancel the Process")
        self.btn_cancel.setIcon(QIcon())
        self.btn_cancel.setIconSize(QSize(20,20))
        self.btn_cancel.setFlat(False)
        self.btn_cancel.move(324, 207)
        self.btn_cancel.setFixedSize(90, 30)
        
        self.btn_pause_play.setText("")
        self.btn_pause_play.setToolTip("Pause/Play")
        self.btn_pause_play.setIconSize(QSize(48, 48))
        self.btn_pause_play.setFlat(True)
        self.btn_pause_play.move(70, 170)
        self.btn_pause_play.setFixedSize(30, 30)
        
        self.btn_mute_unmute.setText("")
        self.btn_mute_unmute.setToolTip("Mute/Unmute")
        self.btn_mute_unmute.setIconSize(QSize(32, 32))
        self.btn_mute_unmute.setFlat(True)
        self.btn_mute_unmute.move(170, 170)
        self.btn_mute_unmute.setFixedSize(30, 30)
        
        self.btn_collapse_expand.setText("")
        self.btn_collapse_expand.setToolTip("Collapse/Expand Window")
        self.btn_collapse_expand.setIcon(QIcon('Icons\collapse-icon.png'))
        self.btn_collapse_expand.setIconSize(QSize(32, 32))
        self.btn_collapse_expand.setFlat(True)
        self.btn_collapse_expand.move(262, 170)
        self.btn_collapse_expand.setFixedSize(30, 30)



        self.btn_start.show()
        self.btn_break.show()
        self.btn_long_break.show()
        self.btn_cancel.show()
       
        self.work_spinbox.show()
        self.break_spinbox.show()
        self.long_break_spinbox.show()
        self.btn_reset.show()    
        
        self.btn_info.show()
        self.btn_qt_info.show()
    #    self.btn_quit.show()
        self.btn_clock.show()
        
        
        
        
def labelCollapse(self):
    if self.flagLabelCollapse == 0 and self.flagCollapseExpandWindow == 1:
        self.flagLabelCollapse = 1
        
        if self.workIsStarted==0 and self.breakIsStarted==0 and self.longBreakIsStarted==0:
            self.min_label.hide()
            self.sec_label.hide()
            self.label1.hide()
            self.system_time_label_2.show()
            self.system_time_label_2.move(0,0)
            self.system_time_label_2.setFixedSize(160, 53)
        else:
            self.min_label.show()
            self.sec_label.show()
            self.label1.show()
            self.system_time_label_2.hide()
            
        
        self.resize(40, 30)
        self.setFixedWidth(159)
        self.setFixedHeight(53)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.showNormal()
        
        # set times label font, size, position
        self.min_label.setFont(QFont("Sansserif", 40, QFont.Weight.Bold))
        self.sec_label.setFont(QFont("Sansserif", 40, QFont.Weight.Bold))
        self.label1.setFont(QFont("Sansserif", 40, QFont.Weight.Bold))
        self.min_label.setFixedSize(70, 50)
        self.sec_label.setFixedSize(70, 50)
        self.label1.setFixedSize(18, 50)
        self.min_label.move(1,1)
        self.sec_label.move(88, 1)
        self.label1.move(70, 1)
        
        if self.dialog_checkbox_lcd.isChecked():
            self.min_label.hide()
            self.sec_label.hide()
            self.min_lcd_number.show()
            self.sec_lcd_number.show()
        else:
            self.min_label.show()
            self.sec_label.show()
            self.min_lcd_number.hide()
            self.sec_lcd_number.hide()
        
        self.min_lcd_number.setFixedSize(70, 50)
        self.sec_lcd_number.setFixedSize(70, 50)
        self.min_lcd_number.move(1,1)
        self.sec_lcd_number.move(88, 1)
        
        self.btn_start.hide()
        self.btn_break.hide()
        self.btn_long_break.hide()
        self.btn_cancel.hide()
        self.btn_mute_unmute.hide()
        self.btn_collapse_expand.hide()
        
        
        
    else:
        if self.flagCollapseExpandWindow == 1:
            # set flag value
            self.flagLabelCollapse = 0
            self.flagCollapseExpandWindow = 1
            
            # set window geometry
            self.resize(100,40)
            self.setFixedWidth(248)
            self.setFixedHeight(140)
            self.setWindowFlag(Qt.WindowType.FramelessWindowHint, False)
            self.showNormal()
            
            if self.dialog_checkbox_stay_on_top.isChecked():
                self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
                self.showNormal()
            if not self.dialog_checkbox_stay_on_top.isChecked():
                self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)
                self.showNormal()
            
            # set times label font, size, position
            self.min_label.setFont(QFont("Sansserif", 60, QFont.Weight.Bold))
            self.sec_label.setFont(QFont("Sansserif", 60, QFont.Weight.Bold))
            self.label1.setFont(QFont("Sansserif", 60, QFont.Weight.Bold))
            self.min_label.setFixedSize(100, 70)
            self.sec_label.setFixedSize(100, 70)
            self.label1.setFixedSize(28, 70)
            self.min_label.move(10,10)
            self.sec_label.move(138, 10)
            self.label1.move(110, 10)
            
            self.label1.show()
            
            if self.dialog_checkbox_lcd.isChecked():
                self.min_label.hide()
                self.sec_label.hide()
                self.min_lcd_number.show()
                self.sec_lcd_number.show()
            else:
                self.min_label.show()
                self.sec_label.show()
                self.min_lcd_number.hide()
                self.sec_lcd_number.hide()
            
            self.min_lcd_number.setFixedSize(100, 70)
            self.sec_lcd_number.setFixedSize(100, 70)
            self.min_lcd_number.move(15,10)
            self.sec_lcd_number.move(138, 10)
            
            self.system_time_label_2.hide()
            self.btn_start.show()
            self.btn_break.show()
            self.btn_long_break.show()
            self.btn_cancel.show()
            self.btn_mute_unmute.show()
            self.btn_collapse_expand.show()

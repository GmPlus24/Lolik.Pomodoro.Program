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


def mySystemTray(self):
    # system tray icon context menu actions
    self.tray_show_app = QAction("Show App", self)
    self.tray_show_app.setIcon(QIcon('Icons\monitor-icon.png'))
    
    self.tray_cancel_process = QAction("Cancel Process", self)
    self.tray_cancel_process.setIcon(QIcon('Icons\cancel-icon.png'))
    self.tray_cancel_process.setFont(QFont("Sansserif", 9, QFont.Weight.Bold))
    self.tray_cancel_process.setEnabled(False)
    
    self.tray_start_action = QAction("Start", self)
    self.tray_start_action.setIcon(QIcon('Icons\start-icon.png'))
    
    self.tray_break_action = QAction("Break", self)
    self.tray_break_action.setIcon(QIcon('Icons\icons8-break-48.png'))
    
    self.tray_long_break_action = QAction("Long Break", self)
    self.tray_long_break_action.setIcon(QIcon('Icons\long-break-icon.png'))
    
    self.tray_quit_action = QAction("Quit", self)
    self.tray_quit_action.setIcon(QIcon('Icons\quit-icon.png'))
    
    
    # system tray icon context menu
    tray_context_menu = QMenu()
    tray_context_menu.addAction(self.tray_show_app)
    tray_context_menu.addSeparator()
    tray_context_menu.addAction(self.tray_cancel_process)
    tray_context_menu.addAction(self.tray_start_action)
    tray_context_menu.addAction(self.tray_break_action)
    tray_context_menu.addAction(self.tray_long_break_action)
    tray_context_menu.addSeparator()
    tray_context_menu.addAction(self.tray_quit_action)
    
    # system tray icon
    self.tray = QSystemTrayIcon(self)
    self.tray.setIcon(QIcon("Icons\Lolik-MainIcon.png"))
    self.tray.setToolTip(self.program_name)
    self.tray.setContextMenu(tray_context_menu)
    self.tray.setVisible(True)
    self.tray.show()
    
    # show message
    self.tray.showMessage(self.program_name, "Welcome to " + self.program_name + "\nA Comfort, Flexible, Easy and Nice  Pomodoro program." )
    
    
def onTrayIconActivated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.ActivationReason.Trigger:
            print(">>> system tray icon clicked")
            
        if reason == QtWidgets.QSystemTrayIcon.ActivationReason.DoubleClick:
            print(">>> system tray icon double clicked")
            self.show_app()
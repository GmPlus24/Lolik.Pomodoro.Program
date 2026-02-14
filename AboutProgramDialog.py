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


#QIcon(":/icons/icons8-pause-48.png"

def aboutProgramDialog(self):
    self.information_dialog = QDialog()
    self.information_dialog.setWindowTitle("About Lolik")
    self.information_dialog.setWindowIcon(QIcon("Icons\Lolik-MainIcon-Small.png"))
    self.information_dialog.resize(1024,640)
    self.setFixedWidth(1024)
    self.setFixedHeight(640)
    
    self.info_dialog_lbl1 = QLabel(self.information_dialog)
    self.info_dialog_lbl1.setPixmap(QPixmap("Icons\Lolik-MainIcon-Small.png"))
    self.info_dialog_lbl1.move(13,30)
    
    self.info_dialog_lbl_Version = QLabel(self.information_dialog)
    #self.info_dialog_lbl_Version = "\n\tVersion: 0.1.0 (2024100300)"
    self.info_dialog_lbl_Version = "\n\tVersion: 0.1.0 (2024100300)  \t[04.07.2024 ~ 04.10.2024]"
    
    self.info_dialog_lbl2 = QLabel(self.information_dialog)
    self.info_dialog_lbl2.setText(self.info_dialog_lbl_Version + "\n\nLolik is a user-friendly Pomodoro program designed to help you stay focused and productive.\nWith Lolik, you can easily break down your work into manageable intervals and track your progress.\nGet ready to take control of your time and boost your productivity with Lolik.\nMade with ❤️ By Gm.\nGitHub: \n\n\nIcons \nSounds\n\n\nThis program is distributed in the hope that it will be useful, but WITHOUT\nANY WARRANTY; without even the implied warranty of MERCHANTABILITY\nor FITNESS FOR A PARTICULAR PURPOSE.\n\nPlease note that the developer of this program is not responsible for any misuse or unintended\nconsequences resulting from the use of this application. Users are advised to exercise caution and use\nthe program responsibly.\n\nلطفا توجه داشته باشید که توسعه دهنده این برنامه مسئولیتی در قبال هرگونه سوء استفاده یا\nعواقب ناخواسته ناشی از استفاده از این برنامه ندارد.به کاربران توصیه می شود\nاحتیاط کنند و از برنامه مسئولانه استفاده کنند.\n\nCC License: Lolik © 2024 by Gm is licensed under CC BY-SA 4.0")
    font = self.info_dialog_lbl2.font()
    font.setPointSize(12)
    self.info_dialog_lbl2.setFont(font)
    self.info_dialog_lbl2.move(265,15)

    self.info_dialog_lbl5 = QLabel(self.information_dialog)
    self.info_dialog_lbl5.setText("<a href=\"https://www.github.com\GmPlus24\">https://www.github.com\GmPlus24</a>")
    self.info_dialog_lbl5.setOpenExternalLinks(True)
    self.info_dialog_lbl5.setFont(font)
    self.info_dialog_lbl5.move(330,161)
    
    self.info_dialog_lbl3 = QLabel(self.information_dialog)
    self.info_dialog_lbl3.setText("<a href=\"https://www.icons8.com\">https://www.icons8.com</a>")
    self.info_dialog_lbl3.setOpenExternalLinks(True)
    self.info_dialog_lbl3.setFont(font)
    self.info_dialog_lbl3.move(370,225)
    
    self.info_dialog_lbl4 = QLabel(self.information_dialog)
    self.info_dialog_lbl4.setText("<a href=\"https://mixkit.co\">https://mixkit.co</a>")
    self.info_dialog_lbl4.setOpenExternalLinks(True)
    self.info_dialog_lbl4.setFont(font)
    self.info_dialog_lbl4.move(370,245)
    
    
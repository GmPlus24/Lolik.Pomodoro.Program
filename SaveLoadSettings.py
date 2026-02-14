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




def load_settings(self):

    self.mySounds() # include sounds
    


    # load settings
    self.settings = QSettings("LolikSettings.ini", QSettings.Format.IniFormat) # load INI file

    if (self.settings.value("WorkTime") ==  None or self.settings.value("BreakTime") ==  None or self.settings.value("LongBreakTime") ==  None or self.settings.value("Process") ==  None or self.settings.value("Sound1") ==  None or self.settings.value("Sound2") ==  None or self.settings.value("Sound3") ==  None or self.settings.value("Repeat") ==  None or self.settings.value("MessageBox") ==  None or self.settings.value("MuteUnmute") ==  None or self.settings.value("LabelFont") ==  None or self.settings.value("CollapseFlag") ==  None or self.settings.value("CollapseLabelSize") ==  None):
    

    
        # set default value
        self.work_spinbox.setValue(25)
        self.break_spinbox.setValue(5)
        self.long_break_spinbox.setValue(30)
        
        # set process mode
        self.process_combobox.setCurrentIndex(0)
        self.process_mode = "AUTO - CONTINUOUS"
        
        # set dialog settings
        self.dialog_combobox_work_sound.setCurrentIndex(2)
        self.dialog_combobox_break_sound.setCurrentIndex(4)
        self.dialog_combobox_long_break_sound.setCurrentIndex(3)
        self.dialog_spinbox_repeat.setValue(5)
        self.dialog_checkbox_messagebox.setChecked(True)
        self.start_sound = 2
        self.break_sound = 4
        self.long_break_sound = 3
        self.message_box_check = "CHECK"
        

        # Set <<Break Button>> and <<Long Break Button>> Disabled, for mode-> Auto
        self.btn_break.setEnabled(False)
        self.btn_long_break.setEnabled(False)
        self.tray_break_action.setEnabled(False)
        self.tray_long_break_action.setEnabled(False)
        
        
        
        # save default value
        self.settings.setValue("WorkTime", 25)
        self.settings.setValue("BreakTime", 5)
        self.settings.setValue("LongBreakTime", 30)
        
        self.settings.setValue("Process", 0)
        self.settings.setValue("Sound1", 2)
        self.settings.setValue("Sound2", 4)
        self.settings.setValue("Sound3", 3)
        self.settings.setValue("Repeat", 5)
        self.settings.setValue("MessageBox", "CHECK")
        
        
        
        # set mute/unmute value
        self.flagMuteUnmuteSound = 0
        self.btn_mute_unmute.setIcon(QIcon("Icons\icons8-sound-48.png"))
        self.settings.setValue("MuteUnmute", 0)
        
        
        
        # display settings
        self.labelFont = "NORMAL"
        self.dialog_checkbox_lcd.setChecked(False)
        self.min_lcd_number.hide()
        self.sec_lcd_number.hide()
        self.min_label.show()
        self.sec_label.show()
        self.settings.setValue("LabelFont", "NORMAL")
        
        
        self.windowCollapseModeFlag = "TOP"
        self.dialog_checkbox_stay_on_top.setChecked(True)
        self.settings.setValue("LabelFont", "TOP")
        
        self.windowCollapseModeFontSize = 60
        self.dialog_spinbox_collapse_font_size.setValue(60)
        self.settings.setValue("CollapseLabelSize", "60")
        
        
        
        
        
        
        
        
    else:
        # set mute/unmute value
        if self.settings.value("MuteUnmute") == "0":
            self.effect1.setVolume(0.75)
            self.effect2.setVolume(0.75)
            self.effect3.setVolume(0.75)
            self.flagMuteUnmuteSound = 0
            self.btn_mute_unmute.setIcon(QIcon("Icons\icons8-sound-48.png"))
        if self.settings.value("MuteUnmute") ==  "1":
            self.effect1.setVolume(0)
            self.effect2.setVolume(0)
            self.effect3.setVolume(0)
            self.flagMuteUnmuteSound = 1
            self.btn_mute_unmute.setIcon(QIcon("Icons\mute-icon.png"))
        
    
        # read values and set program main values
        self.work_spinbox.setValue(int(self.settings.value("WorkTime")))
        self.break_spinbox.setValue(int(self.settings.value("BreakTime")))
        self.long_break_spinbox.setValue(int(self.settings.value("LongBreakTime")))

        self.process_combobox.setCurrentIndex(int(self.settings.value("Process")))
        
        self.dialog_combobox_work_sound.setCurrentIndex(int(self.settings.value("Sound1")))
        self.dialog_combobox_break_sound.setCurrentIndex(int(self.settings.value("Sound2")))
        self.dialog_combobox_long_break_sound.setCurrentIndex(int(self.settings.value("Sound3")))
        self.dialog_spinbox_repeat.setValue(int(self.settings.value("Repeat")))



        # Set <<Break Button>> and <<Long Break Button>> Disabled, for mode -> Auto
        if int(self.settings.value("Process")) == 0:
            self.btn_break.setEnabled(False)
            self.btn_long_break.setEnabled(False)
            self.tray_break_action.setEnabled(False)
            self.tray_long_break_action.setEnabled(False)
            self.process_mode = "AUTO - CONTINUOUS"

        if int(self.settings.value("Process")) == 1:
            self.btn_break.setEnabled(True)
            self.btn_long_break.setEnabled(True)
            self.tray_break_action.setEnabled(True)
            self.tray_long_break_action.setEnabled(True)
            self.process_mode = "SINGLE SHOT"





    # change buttons color
    self.btn_start.setStyleSheet('background-color:rgb(63, 186, 41);')
    self.btn_cancel.setStyleSheet('background-color:rgb();')
    if self.process_combobox.currentText() == "Single Shot":
        self.btn_break.setStyleSheet('background-color:rgb(63, 186, 41);')
        self.btn_long_break.setStyleSheet('background-color:rgb(63, 186, 41);')
    else:
        self.btn_break.setStyleSheet('background-color:rgb();')
        self.btn_long_break.setStyleSheet('background-color:rgb();')

    
    

    # --------- Set Values in QSoundEffect Object --------- 
    # set sound
    user_sound = self.dialog_combobox_work_sound.currentText()
    if user_sound == "Ring Sound Effect":
        self.effect1.setSource(QUrl.fromLocalFile("Sounds\Ring-sound-effect.wav"))
        self.start_sound = 0
    if user_sound == "Emergency Alarm":
        self.effect1.setSource(QUrl.fromLocalFile("Sounds\Emergency-alarm.wav"))
        self.start_sound = 1
    if user_sound == "Data Scaner":
        self.effect1.setSource(QUrl.fromLocalFile("Sounds\Data-scaner.wav"))
        self.start_sound = 2
    if user_sound == "Security Facility Breach Alarm":
        self.effect1.setSource(QUrl.fromLocalFile("Sounds\security-facility-breach-alarm.wav"))
        self.start_sound = 3
    if user_sound == "Smartphone Ringtone":
        self.effect1.setSource(QUrl.fromLocalFile("Sounds\smartphone-ringtone.wav"))
        self.start_sound = 4
        
        
    user_sound2 = self.dialog_combobox_break_sound.currentText()
    if user_sound2 == "Ring Sound Effect":
        self.effect2.setSource(QUrl.fromLocalFile("Sounds\Ring-sound-effect.wav"))
        self.break_sound = 0
    if user_sound2 == "Emergency Alarm":
        self.effect2.setSource(QUrl.fromLocalFile("Sounds\Emergency-alarm.wav"))
        self.break_sound = 1
    if user_sound2 == "Data Scaner":
        self.effect2.setSource(QUrl.fromLocalFile("Sounds\Data-scaner.wav"))
        self.break_sound = 2
    if user_sound2 == "Security Facility Breach Alarm":
        self.effect2.setSource(QUrl.fromLocalFile("Sounds\security-facility-breach-alarm.wav"))
        self.break_sound = 3
    if user_sound2 == "Smartphone Ringtone":
        self.effect2.setSource(QUrl.fromLocalFile("Sounds\smartphone-ringtone.wav"))
        self.break_sound = 4
    
    
    user_sound3 = self.dialog_combobox_long_break_sound.currentText()
    if user_sound3 == "Ring Sound Effect":
        self.effect3.setSource(QUrl.fromLocalFile("Sounds\Ring-sound-effect.wav"))
        self.long_break_sound = 0
    if user_sound3 == "Emergency Alarm":
        self.effect3.setSource(QUrl.fromLocalFile("Sounds\Emergency-alarm.wav"))
        self.long_break_sound = 1
    if user_sound3 == "Data Scaner":
        self.effect3.setSource(QUrl.fromLocalFile("Sounds\Data-scaner.wav"))
        self.long_break_sound = 2
    if user_sound3 == "Security Facility Breach Alarm":
        self.effect3.setSource(QUrl.fromLocalFile("Sounds\security-facility-breach-alarm.wav"))
        self.long_break_sound = 3
    if user_sound3 == "Smartphone Ringtone":
        self.effect3.setSource(QUrl.fromLocalFile("Sounds\smartphone-ringtone.wav"))
        self.long_break_sound = 4
        
    # set repeat
    user_repeat = self.dialog_spinbox_repeat.value()
    self.effect1.setLoopCount(user_repeat)
    self.effect2.setLoopCount(user_repeat)
    self.effect3.setLoopCount(user_repeat)
    self.times_for_repeat = self.dialog_spinbox_repeat.value()
    
    
        
    if self.settings.value("MessageBox") == "CHECK":
        self.dialog_checkbox_messagebox.setChecked(True)
        self.message_box_check = "CHECK"
        
    if self.settings.value("MessageBox") == "NOT CHECK":
        self.dialog_checkbox_messagebox.setChecked(False)
        self.message_box_check = "NOT CHECK"
        
        
        
        
        
    # display Settings
    if self.settings.value("LabelFont") == "NORMAL":
        self.labelFont = "NORMAL"
        self.dialog_checkbox_lcd.setChecked(False)
        self.min_lcd_number.hide()
        self.sec_lcd_number.hide()
        self.min_label.show()
        self.sec_label.show()
    if self.settings.value("LabelFont") == "LCD":
        self.labelFont = "LCD"
        self.dialog_checkbox_lcd.setChecked(True)
        self.min_lcd_number.show()
        self.sec_lcd_number.show()
        self.min_label.hide()
        self.sec_label.hide()
    
    if self.settings.value("CollapseFlag") == "NORMAL":
        self.windowCollapseModeFlag = "NORMAL"
        self.dialog_checkbox_stay_on_top.setChecked(False)
    if self.settings.value("CollapseFlag") == "TOP":
        self.windowCollapseModeFlag = "TOP"
        self.dialog_checkbox_stay_on_top.setChecked(True)   
        
    self.windowCollapseModeFontSize = self.settings.value("CollapseLabelSize")
    self.dialog_spinbox_collapse_font_size.setValue(int(self.windowCollapseModeFontSize))






#----------------------------------------------------------------------------------------------------------------------------------------------    
def save_settings(self):
    # set values
    self.settings.setValue("WorkTime", str(self.work_spinbox.value()))
    self.settings.setValue("BreakTime", str(self.break_spinbox.value()))
    self.settings.setValue("LongBreakTime", str(self.long_break_spinbox.value()))
    
    self.settings.setValue("Process", self.process_combobox.currentIndex())
    self.settings.setValue("Sound1", self.dialog_combobox_work_sound.currentIndex())
    self.settings.setValue("Sound2", self.dialog_combobox_break_sound.currentIndex())
    self.settings.setValue("Sound3", self.dialog_combobox_long_break_sound.currentIndex())
    self.settings.setValue("Repeat", self.dialog_spinbox_repeat.value())
    
    self.settings.setValue("MuteUnmute", self.flagMuteUnmuteSound)
    
    if self.dialog_checkbox_messagebox.isChecked():
        self.settings.setValue("MessageBox", "CHECK")    
    else:
        self.settings.setValue("MessageBox", "NOT CHECK")
        
    
    
    # display settings
    if self.dialog_checkbox_lcd.isChecked():
        self.settings.setValue("LabelFont", "LCD")
    else:
        self.settings.setValue("LabelFont", "NORMAL")
    if self.dialog_checkbox_stay_on_top.isChecked():
        self.settings.setValue("CollapseFlag", "TOP")
    else:
        self.settings.setValue("CollapseFlag", "NORMAL")
    self.settings.setValue("CollapseLabelSize", str(self.dialog_spinbox_collapse_font_size.value()))
    
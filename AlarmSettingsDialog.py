from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QToolButton, QMessageBox, QDialog, QSystemTrayIcon, QMenu, QSpinBox, QComboBox, QCheckBox, QSplashScreen, QStatusBar, QTabWidget, QWidget
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

from GlobalSounds import mySounds


def myAlarmSettingsDialog(self):
    self.mySounds() # include sounds
    
    # --------------------------- change alarm settings Dialog ---------------------------
    # create alarm settings dialog
    self.alarm_settings_dialog = QDialog(self)
    self.alarm_settings_dialog.setWindowTitle("Settings")
    self.alarm_settings_dialog.setWindowIcon(QIcon("Icons\settings-icon.png"))
    self.alarm_settings_dialog.resize(350,160)
    self.alarm_settings_dialog.setFixedSize(455,300)
    
    self.tab1 = QWidget()
    self.tab2 = QWidget()
    
    self.myTabWidget = QTabWidget(self.alarm_settings_dialog)
    self.myTabWidget.addTab(self.tab1, "Alarm")
    self.myTabWidget.addTab(self.tab2, "Display")
    self.myTabWidget.move(5,5)
    self.myTabWidget.setFixedSize(450,250)
    
    
    self.dialog_lbl_sound = QLabel("Sound", self.tab1)
    font = self.dialog_lbl_sound.font()
    font.setPointSize(10)
    font.setBold(True)
    self.dialog_lbl_sound.setFont(font)
    self.dialog_lbl_sound.move(10, 15)
    
    self.dialog_lbl_work_sound = QLabel("Work Sound:", self.tab1)
    self.dialog_lbl_work_sound.setToolTip("Work Sound")
    self.dialog_lbl_work_sound.move(10, 42)
    self.dialog_combobox_work_sound = QComboBox(self.tab1)
    self.dialog_combobox_work_sound.setToolTip("Set Work Sound")
    self.dialog_combobox_work_sound.addItem("Ring Sound Effect")
    self.dialog_combobox_work_sound.addItem("Emergency Alarm")
    self.dialog_combobox_work_sound.addItem("Data Scaner")
    self.dialog_combobox_work_sound.addItem("Security Facility Breach Alarm")
    self.dialog_combobox_work_sound.addItem("Smartphone Ringtone")
    self.dialog_combobox_work_sound.setFixedSize(265, 23)
    self.dialog_combobox_work_sound.move(117, 40)
    self.dialog_btn_play_sound_1 = QPushButton(self.tab1)
    self.dialog_btn_play_sound_1.setToolTip("Play Sound")
    self.dialog_btn_play_sound_1.setIcon(QIcon('Icons\start-icon.png'))
    self.dialog_btn_play_sound_1.setAutoDefault(False)
    self.dialog_btn_play_sound_1.move(385, 40)
    self.dialog_btn_stop_sound_1 = QPushButton(self.tab1)
    self.dialog_btn_stop_sound_1.setToolTip("Stop Sound")
    self.dialog_btn_stop_sound_1.setIcon(QIcon('Icons\stop-icon.png'))
    self.dialog_btn_stop_sound_1.setEnabled(False)
    self.dialog_btn_stop_sound_1.setAutoDefault(False)
    self.dialog_btn_stop_sound_1.move(415, 40)
    
    
    self.dialog_lbl_break_sound = QLabel("Break Sound:", self.tab1)
    self.dialog_lbl_break_sound.setToolTip("Break Sound")
    self.dialog_lbl_break_sound.move(10, 69)
    self.dialog_combobox_break_sound = QComboBox(self.tab1)
    self.dialog_combobox_break_sound.setToolTip("Set Break Sound")
    self.dialog_combobox_break_sound.addItem("Ring Sound Effect")
    self.dialog_combobox_break_sound.addItem("Emergency Alarm")
    self.dialog_combobox_break_sound.addItem("Data Scaner")
    self.dialog_combobox_break_sound.addItem("Security Facility Breach Alarm")
    self.dialog_combobox_break_sound.addItem("Smartphone Ringtone")
    self.dialog_combobox_break_sound.setFixedSize(265, 23)
    self.dialog_combobox_break_sound.move(117, 67)
    self.dialog_btn_play_sound_2 = QPushButton(self.tab1)
    self.dialog_btn_play_sound_2.setToolTip("Play Sound")
    self.dialog_btn_play_sound_2.setIcon(QIcon('Icons\start-icon.png'))
    self.dialog_btn_play_sound_2.setAutoDefault(False)
    self.dialog_btn_play_sound_2.move(385, 67)
    self.dialog_btn_stop_sound_2 = QPushButton(self.tab1)
    self.dialog_btn_stop_sound_2.setToolTip("Stop Sound")
    self.dialog_btn_stop_sound_2.setIcon(QIcon('Icons\stop-icon.png'))
    self.dialog_btn_stop_sound_2.setEnabled(False)
    self.dialog_btn_stop_sound_2.setAutoDefault(False)
    self.dialog_btn_stop_sound_2.move(415, 67)
    
   
    self.dialog_lbl_long_break_sound = QLabel("Long Break Sound:", self.tab1)
    self.dialog_lbl_long_break_sound.setToolTip("Long Break Sound")
    self.dialog_lbl_long_break_sound.move(10, 96)
    self.dialog_combobox_long_break_sound = QComboBox(self.tab1)
    self.dialog_combobox_long_break_sound.setToolTip("Set Long Break Sound")
    self.dialog_combobox_long_break_sound.addItem("Ring Sound Effect")
    self.dialog_combobox_long_break_sound.addItem("Emergency Alarm")
    self.dialog_combobox_long_break_sound.addItem("Data Scaner")
    self.dialog_combobox_long_break_sound.addItem("Security Facility Breach Alarm")
    self.dialog_combobox_long_break_sound.addItem("Smartphone Ringtone")
    self.dialog_combobox_long_break_sound.setFixedSize(265, 23)
    self.dialog_combobox_long_break_sound.move(117, 94)
    self.dialog_btn_play_sound_3 = QPushButton(self.tab1)
    self.dialog_btn_play_sound_3.setToolTip("Play Sound")
    self.dialog_btn_play_sound_3.setIcon(QIcon('Icons\start-icon.png'))
    self.dialog_btn_play_sound_3.setAutoDefault(False)
    self.dialog_btn_play_sound_3.move(385, 94)
    self.dialog_btn_stop_sound_3 = QPushButton(self.tab1)
    self.dialog_btn_stop_sound_3.setToolTip("Stop Sound")
    self.dialog_btn_stop_sound_3.setIcon(QIcon('Icons\stop-icon.png'))
    self.dialog_btn_stop_sound_3.setEnabled(False)
    self.dialog_btn_stop_sound_3.setAutoDefault(False)
    self.dialog_btn_stop_sound_3.move(415, 94)
    
    
    self.dialog_lbl_repeat = QLabel("Sound Repeat:", self.tab1)
    self.dialog_lbl_repeat.setToolTip("Sound Repeat")
    self.dialog_lbl_repeat.move(10, 121)
    
    self.dialog_spinbox_repeat = QSpinBox(self.tab1)
    self.dialog_spinbox_repeat.setToolTip("Set Repeat")
    self.dialog_spinbox_repeat.setValue(5)
    self.dialog_spinbox_repeat.setRange(1, 100)
    self.dialog_spinbox_repeat.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.dialog_spinbox_repeat.setFixedSize(326, 23)
    self.dialog_spinbox_repeat.move(117, 121)
    
    
    
    
    self.dialog_lbl_message_box = QLabel("Message Box", self.tab1)
    font2 = self.dialog_lbl_message_box.font()
    font2.setPointSize(10)
    font2.setBold(True)
    self.dialog_lbl_message_box.setFont(font2)
    self.dialog_lbl_message_box.move(10, 165)
    
    self.dialog_checkbox_messagebox = QCheckBox("Show message box when process finished", self.tab1)
    self.dialog_checkbox_messagebox.setToolTip("Show message box when process finished")
    self.dialog_checkbox_messagebox.setChecked(True)
    self.dialog_checkbox_messagebox.move(10, 188)
    
    
    
    
    
    # tab --> display
    self.dialog_lbl_label = QLabel("Label", self.tab2)
    font = self.dialog_lbl_label.font()
    font.setPointSize(10)
    font.setBold(True)
    self.dialog_lbl_label.setFont(font)
    self.dialog_lbl_label.move(10, 15)
    
    self.dialog_checkbox_lcd = QCheckBox("LCD Display", self.tab2)
    self.dialog_checkbox_lcd.setToolTip("LCD Display")
    self.dialog_checkbox_lcd.setChecked(True)
    self.dialog_checkbox_lcd.move(10, 42)
    
    
    self.dialog_lbl_window = QLabel("Window", self.tab2)
    font = self.dialog_lbl_window.font()
    font.setPointSize(10)
    font.setBold(True)
    self.dialog_lbl_window.setFont(font)
    self.dialog_lbl_window.move(10, 100)
    
    self.dialog_checkbox_stay_on_top = QCheckBox("On Collapse Mode, Stay on Top", self.tab2)
    self.dialog_checkbox_stay_on_top.setToolTip("On Collapse Mode, Stay on Top")
    self.dialog_checkbox_stay_on_top.setChecked(True)
    self.dialog_checkbox_stay_on_top.move(10, 127)
    
    

    self.dialog_lbl_collapse_font_size = QLabel("Collapse Font Size:", self.tab2)
    self.dialog_lbl_collapse_font_size.setToolTip("Collapse Font Size")
    self.dialog_lbl_collapse_font_size.move(10, 157)
    self.dialog_lbl_collapse_font_size.hide()
    
    self.dialog_spinbox_collapse_font_size = QSpinBox(self.tab2)
    self.dialog_spinbox_collapse_font_size.setToolTip("Collapse Font Size")
    self.dialog_spinbox_collapse_font_size.setValue(60)
    self.dialog_spinbox_collapse_font_size.setRange(20, 100)
    self.dialog_spinbox_collapse_font_size.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.dialog_spinbox_collapse_font_size.setFixedSize(326, 23)
    self.dialog_spinbox_collapse_font_size.move(115, 156)
    self.dialog_spinbox_collapse_font_size.hide()

    
    
    
    # OK and Cancel and load defaults buttons
    self.dialog_btn_ok = QPushButton("OK", self.alarm_settings_dialog)
    self.dialog_btn_ok.setToolTip("OK")
    self.dialog_btn_ok.setFixedSize(80, 30)
    self.dialog_btn_ok.move(278, 265)
    
    self.dialog_btn_cancel = QPushButton("Cancel", self.alarm_settings_dialog)
    self.dialog_btn_cancel.setToolTip("Cancel")
    self.dialog_btn_cancel.setFixedSize(80, 30)
    self.dialog_btn_cancel.move(363, 265)
    
    self.dialog_btn_load_defaults = QPushButton("Load all Defaults", self.alarm_settings_dialog)
    self.dialog_btn_load_defaults.setToolTip("Load all Defaults")
    self.dialog_btn_load_defaults.setFixedSize(100, 30)
    self.dialog_btn_load_defaults.move(173, 265)
    # change alarm settings Dialog -----------------------------------------------------
    

    # set current settings, read all alarm settings from alarm settings dialog
    # set process
    if self.process_combobox.currentIndex() == 0:
        self.process_mode = "AUTO"
    if self.process_combobox.currentIndex() == 1:
        self.process_mode = "SINGLE SHOT"
    
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
    
    
        
    if self.dialog_checkbox_messagebox.isChecked():
        self.dialog_checkbox_messagebox.setChecked(True)
        self.message_box_check = "CHECK"
        
    if not self.dialog_checkbox_messagebox.isChecked():
        self.dialog_checkbox_messagebox.setChecked(False)
        self.message_box_check = "NOT CHECK"





def alarm_settings(self):
    # show menu
    self.alarm_settings_dialog.exec()

def dialog_ok(self):
    print(">>> OK Button Clicked")
    
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
    
    
        
    if self.dialog_checkbox_messagebox.isChecked():
        self.dialog_checkbox_messagebox.setChecked(True)
        self.message_box_check = "CHECK"
        
    if not self.dialog_checkbox_messagebox.isChecked():
        self.dialog_checkbox_messagebox.setChecked(False)
        self.message_box_check = "NOT CHECK"
        
    
    if self.dialog_checkbox_lcd.isChecked():
        self.min_lcd_number.show()
        self.sec_lcd_number.show()
        self.min_label.hide()
        self.sec_label.hide()
    if not self.dialog_checkbox_lcd.isChecked():
        self.min_lcd_number.hide()
        self.sec_lcd_number.hide()
        self.min_label.show()
        self.sec_label.show()
    
    
    # save settings
    self.save_settings()
    # close dialog
    self.alarm_settings_dialog.close()
    
    
def dialog_cancel(self):
    print(">>> cancel button clicked")
    
    self.dialog_combobox_work_sound.setCurrentIndex(self.start_sound)
    self.dialog_combobox_break_sound.setCurrentIndex(self.break_sound)
    self.dialog_combobox_long_break_sound.setCurrentIndex(self.long_break_sound)
    self.dialog_spinbox_repeat.setValue(self.times_for_repeat)
    
    if self.message_box_check == "CHECK":
        self.dialog_checkbox_messagebox.setChecked(True)
    if self.message_box_check == "NOT CHECK":
        self.dialog_checkbox_messagebox.setChecked(False)
        
    self.alarm_settings_dialog.close()
    
    
def dialog_load_defaults(self):
    self.dialog_combobox_work_sound.setCurrentIndex(2)
    self.dialog_combobox_break_sound.setCurrentIndex(4)
    self.dialog_combobox_long_break_sound.setCurrentIndex(3)
    self.dialog_spinbox_repeat.setValue(5)
    self.dialog_checkbox_messagebox.setChecked(True)
    self.dialog_checkbox_lcd.setChecked(False)
    self.dialog_checkbox_stay_on_top.setChecked(True)



def disableStopButton(self):
    self.TimerTestSound.start()
    if self.userTestEffect.isPlaying():
        pass
        
    else:
        self.dialog_btn_stop_sound_1.setEnabled(False)
        self.dialog_btn_stop_sound_2.setEnabled(False)
        self.dialog_btn_stop_sound_3.setEnabled(False)
        self.TimerTestSound.stop()
    
    


def dialog_play_1(self):
    # set sound
    test_user_sound = self.dialog_combobox_work_sound.currentText()
    if test_user_sound == "Ring Sound Effect":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\Ring-sound-effect.wav"))
    if test_user_sound == "Emergency Alarm":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\Emergency-alarm.wav"))
    if test_user_sound == "Data Scaner":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\Data-scaner.wav"))
    if test_user_sound == "Security Facility Breach Alarm":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\security-facility-breach-alarm.wav"))
    if test_user_sound == "Smartphone Ringtone":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\smartphone-ringtone.wav"))
    self.userTestEffect.play()
    self.dialog_btn_stop_sound_1.setEnabled(True) # set stop button enabled
    self.disableStopButton()
    

def dialog_stop_1(self):
    self.userTestEffect.stop() # stop sound
    self.dialog_btn_stop_sound_1.setEnabled(False)  # set stop button disabled
    
    

def dialog_play_2(self):
    # set sound
    test_user_sound = self.dialog_combobox_break_sound.currentText()
    if test_user_sound == "Ring Sound Effect":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\Ring-sound-effect.wav"))
    if test_user_sound == "Emergency Alarm":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\Emergency-alarm.wav"))
    if test_user_sound == "Data Scaner":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\Data-scaner.wav"))
    if test_user_sound == "Security Facility Breach Alarm":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\security-facility-breach-alarm.wav"))
    if test_user_sound == "Smartphone Ringtone":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\smartphone-ringtone.wav"))
    self.userTestEffect.play()
    self.dialog_btn_stop_sound_2.setEnabled(True) # set stop button enabled
    self.disableStopButton()

def dialog_stop_2(self):
    self.userTestEffect.stop() # stop sound
    self.dialog_btn_stop_sound_2.setEnabled(False)  # set stop button disabled



def dialog_play_3(self):
    # set sound
    test_user_sound = self.dialog_combobox_long_break_sound.currentText()
    if test_user_sound == "Ring Sound Effect":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\Ring-sound-effect.wav"))
    if test_user_sound == "Emergency Alarm":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\Emergency-alarm.wav"))
    if test_user_sound == "Data Scaner":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\Data-scaner.wav"))
    if test_user_sound == "Security Facility Breach Alarm":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\security-facility-breach-alarm.wav"))
    if test_user_sound == "Smartphone Ringtone":
        self.userTestEffect.setSource(QUrl.fromLocalFile("Sounds\smartphone-ringtone.wav"))
    self.userTestEffect.play()
    self.dialog_btn_stop_sound_3.setEnabled(True) # set stop button enabled
    self.disableStopButton()

def dialog_stop_3(self):
    self.userTestEffect.stop() # stop sound
    self.dialog_btn_stop_sound_3.setEnabled(False)  # set stop button disabled

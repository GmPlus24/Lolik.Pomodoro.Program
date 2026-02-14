from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QToolButton, QMessageBox, QDialog, QSystemTrayIcon, QMenu, QSpinBox, QComboBox, QCheckBox, QSplashScreen, QStatusBar, QProgressBar
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



class LolikWindow(QMainWindow):

    # import my defines
    from Gui import myGui
    from GlobalVariables import myVariables
    
    from SystemTray import mySystemTray
    from SystemTray import onTrayIconActivated
    
    from TimerProcess import start_work_TimerCallBack
    from TimerProcess import _start_work
    from TimerProcess import start_break_TimerCallBack
    from TimerProcess import _break_work
    from TimerProcess import start_long_break_TimerCallBack
    from TimerProcess import _long_break_work
    
    from SaveLoadSettings import load_settings
    from SaveLoadSettings import save_settings
    
    from AlarmSettingsDialog import myAlarmSettingsDialog
    from AlarmSettingsDialog import alarm_settings
    from AlarmSettingsDialog import dialog_ok
    from AlarmSettingsDialog import dialog_load_defaults
    from AlarmSettingsDialog import dialog_cancel
    from AlarmSettingsDialog import dialog_play_1
    from AlarmSettingsDialog import dialog_stop_1
    from AlarmSettingsDialog import dialog_play_2
    from AlarmSettingsDialog import dialog_stop_2
    from AlarmSettingsDialog import dialog_play_3
    from AlarmSettingsDialog import dialog_stop_3
    from AlarmSettingsDialog import disableStopButton
    
    from GlobalSounds import mySounds
    
    from ProcessFinishedDialog import ProcessFinishedDialog
    from ProcessFinishedDialog import DialogTimerCallBack
    from ProcessFinishedDialog import StartDialogTimer
    from ProcessFinishedDialog import myDialogOk
    
    from AboutProgramDialog import aboutProgramDialog
    
    from CollapseExpandWindow import collapseExpandeWindow
    from CollapseExpandWindow import labelCollapse
    

    def __init__(self , appXX ):
        super().__init__()
        self.app = appXX


        self.flashSplash() # show splash screen
        self.myGui() # import gui
        self.myVariables() # import variables
        self.mySystemTray() # import system tray
        self.myAlarmSettingsDialog() # import alarm settings dialog gui
        self.showTime() # show system time
        self.showTime2() # show system time
        self.mySounds() # include sounds
        self.ProcessFinishedDialog() # import dialog
        self.aboutProgramDialog() # import dialog
        
        
        self.setWindowTitle(self.program_name)
        self.setGeometry(100,100, 450,230)
        self.setWindowIcon(QIcon('Icons\Lolik-MainIcon.png'))
        
        self.setFixedWidth(451)
        self.setFixedHeight(315)
        
        
        if self.debug == 1:
            print(">>> debug mode")
        else:
            print(">>> out of debug mode")
            kernel32 = ctypes.WinDLL('kernel32')
            user32 = ctypes.WinDLL('user32')
            SW_HIDE = 0
            hWnd = kernel32.GetConsoleWindow()
            user32.ShowWindow(hWnd, SW_HIDE)
            

        # connect signal/slots
        self.process_combobox.currentIndexChanged.connect(self.processChanged)
        self.btn_start.clicked.connect(self._start_work)
        self.btn_break.clicked.connect(self._break_work)
        self.btn_long_break.clicked.connect(self._long_break_work)
        self.btn_cancel.clicked.connect(self.cancel_process)
        self.btn_info.clicked.connect(self.show_info)
        self.btn_info.setToolTip("About " + self.program_name)
        self.btn_qt_info.clicked.connect(self.app.aboutQt)
        self.btn_clock.clicked.connect(self.alarm_settings)
        self.btn_collapse_expand.clicked.connect(self.collapseExpandeWindow)
        self.btn_mute_unmute.clicked.connect(self.muteUnmuteSound)
        self.btn_pause_play.clicked.connect(self.pausePlayProcess)
        self.work_spinbox.valueChanged.connect(self.workSpinBoxValueChanged)
        self.break_spinbox.valueChanged.connect(self.save_settings)
        self.long_break_spinbox.valueChanged.connect(self.save_settings)
        self.btn_reset.clicked.connect(self.reset_settings)
        self.min_lcd_number.clicked.connect(self.labelCollapse)
        self.sec_lcd_number.clicked.connect(self.labelCollapse)
        self.min_label.clicked.connect(self.labelCollapse)
        self.sec_label.clicked.connect(self.labelCollapse)
        self.label1.clicked.connect(self.labelCollapse)
        self.system_time_label_2.clicked.connect(self.labelCollapse)
        
        self.tray_show_app.triggered.connect(self.show_app)
        self.tray_cancel_process.triggered.connect(self.cancel_process)
        self.tray_start_action.triggered.connect(self._start_work)
        self.tray_break_action.triggered.connect(self._break_work)
        self.tray_long_break_action.triggered.connect(self._long_break_work)
        self.tray_quit_action.triggered.connect(self._quit)
        self.tray.activated.connect(self.onTrayIconActivated)
        
        self.dialog_btn_play_sound_1.clicked.connect(self.dialog_play_1)
        self.dialog_btn_stop_sound_1.clicked.connect(self.dialog_stop_1)
        self.dialog_btn_play_sound_2.clicked.connect(self.dialog_play_2)
        self.dialog_btn_stop_sound_2.clicked.connect(self.dialog_stop_2)
        self.dialog_btn_play_sound_3.clicked.connect(self.dialog_play_3)
        self.dialog_btn_stop_sound_3.clicked.connect(self.dialog_stop_3)
        self.dialog_btn_ok.clicked.connect(self.dialog_ok)
        self.dialog_btn_cancel.clicked.connect(self.dialog_cancel)
        self.dialog_btn_load_defaults.clicked.connect(self.dialog_load_defaults)
        
        
        
        # Set <<Break Button>> and <<Long Break Button>> Disabled, for mode-> Auto
        self.btn_break.setEnabled(False)
        self.btn_long_break.setEnabled(False)
        self.tray_break_action.setEnabled(False)
        self.tray_long_break_action.setEnabled(False)


     
        # block all signals
        self.work_spinbox.blockSignals(True)  # BLOCK
        self.break_spinbox.blockSignals(True)  # BLOCK
        self.long_break_spinbox.blockSignals(True)  # BLOCK
        self.process_combobox.blockSignals(True)  # BLOCK
        self.dialog_combobox_work_sound.blockSignals(True)  # BLOCK
        self.dialog_spinbox_repeat.blockSignals(True)  # BLOCK
        self.dialog_checkbox_messagebox.blockSignals(True)  # BLOCK
        self.btn_mute_unmute.blockSignals(True)  # BLOCK
        # load settings
        self.load_settings()
        # unblock all signals
        self.work_spinbox.blockSignals(False)  # UN BLOCK
        self.break_spinbox.blockSignals(False)  # UN BLOCK
        self.long_break_spinbox.blockSignals(False)  # UN BLOCK
        self.process_combobox.blockSignals(False)  # UN BLOCK
        self.dialog_combobox_work_sound.blockSignals(False)  # UN BLOCK
        self.dialog_spinbox_repeat.blockSignals(False)  # UN BLOCK
        self.dialog_checkbox_messagebox.blockSignals(False)  # UN BLOCK
        self.btn_mute_unmute.blockSignals(False)  # UN BLOCK
        

        # set the labels text
        if self.work_spinbox.value() > 10:
            self.min_label.setText(str(self.work_spinbox.value()))
            self.min_lcd_number.display(str(self.work_spinbox.value()))
        if self.work_spinbox.value() < 9:
            self.min_label.setText("0" + str(self.work_spinbox.value()))
            self.min_lcd_number.display("0" + str(self.work_spinbox.value()))
        if self.work_spinbox.value() == 10:
            self.min_label.setText(str(self.work_spinbox.value()))
            self.min_lcd_number.display(str(self.work_spinbox.value()))
        if self.work_spinbox.value() == 9:
            self.min_label.setText("0" + str(self.work_spinbox.value()))
            self.min_lcd_number.display("0" + str(self.work_spinbox.value()))
        self.sec_label.setText("00")
        self.sec_lcd_number.display("00")
     


    def flashSplash(self):
        self.splash = QSplashScreen(QPixmap('Icons\Lolik-SplashScreen.png'))
        self.splash.show()
        #QTimer.singleShot(7000, self.splash.close)
        time.sleep(7)
        self.splash.close()
        
        
    
    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if QEvent.Type.WindowStateChange and self.isMinimized:
                #print("WindowMinimized")
                self.hide()

    def closeEvent(self, event):
        print(">>> button x on top of window clicked")
        self.setVisible(False)
        self.hide()
        self.destroy()
        self.close()
        
    def _quit(self):
        print(">>> button quit clicked")
        self.show()
        self.close()    

    def show_app(self):
        self.showNormal()
        
    def showTime(self):
        self.system_time = strftime('%d/%m/%Y \n %H:%M:%S %p')
        self.system_time_label.setText(self.system_time)
        QTimer.singleShot(1000, self.showTime)
    def showTime2(self):
        self.system_time_2 = strftime('%H:%M')
        self.system_time_label_2.setText(self.system_time_2)
        QTimer.singleShot(1000, self.showTime2)

    def processChanged(self):
        self.btn_start.setStyleSheet('background-color:rgb(63, 186, 41);')
        if self.process_combobox.currentText() == "Single Shot":
            self.btn_break.setStyleSheet('background-color:rgb(63, 186, 41);')
            self.btn_long_break.setStyleSheet('background-color:rgb(63, 186, 41);')
        else:
            self.btn_break.setStyleSheet('background-color:rgb();')
            self.btn_long_break.setStyleSheet('background-color:rgb();')
    
        if self.process_combobox.currentIndex() == 0:
            self.btn_break.setEnabled(False) # set disabled
            self.btn_long_break.setEnabled(False) # set disabled
            self.tray_break_action.setEnabled(False)
            self.tray_long_break_action.setEnabled(False)
            self.process_mode = "AUTO - CONTINUOUS"
        if self.process_combobox.currentIndex() == 1:
            self.btn_break.setEnabled(True) # set enabled
            self.btn_long_break.setEnabled(True) # set enabled
            self.tray_break_action.setEnabled(True)
            self.tray_long_break_action.setEnabled(True)
            self.process_mode = "SINGLE SHOT"
        # save settings
        self.save_settings()
        # set status bar
        self.myStatusBar.showMessage("Ready")
        
                
    def workSpinBoxValueChanged(self):
        # set the labels text
        if self.work_spinbox.value() > 10:
            self.min_label.setText(str(self.work_spinbox.value()))
            self.min_lcd_number.display(str(self.work_spinbox.value()))
        if self.work_spinbox.value() < 9:
            self.min_label.setText("0" + str(self.work_spinbox.value()))
            self.min_lcd_number.display("0" + str(self.work_spinbox.value()))
        if self.work_spinbox.value() == 10:
            self.min_label.setText(str(self.work_spinbox.value()))
            self.min_lcd_number.display(str(self.work_spinbox.value()))
        if self.work_spinbox.value() == 9:
            self.min_label.setText("0" + str(self.work_spinbox.value()))
            self.min_lcd_number.display("0" + str(self.work_spinbox.value()))
        self.sec_label.setText("00")
        self.sec_lcd_number.display("00")
        # call save settings
        self.save_settings()

    def reset_settings(self):
        # reset all spin boxs
        self.work_spinbox.setValue(25)
        self.break_spinbox.setValue(5)
        self.long_break_spinbox.setValue(30)
        
    def alarmNotificationTimerCallBack(self):
        self.myAlarmNotification.show()
        if self.alarmVar == 0:
            self.myAlarmNotification.setPixmap(QPixmap("Icons\icons8-notification-bell-24.png"))
            self.myAlarmNotification.setText("")
            self.alarmVar = 1
        else:
            self.myAlarmNotification.setPixmap(QPixmap())
            self.myAlarmNotification.setText("        ")
            self.alarmVar = 0
            
    def alarmNotificationStop(self):
        self.TimerAlarmNotification.stop()
        self.myAlarmNotification.hide()
        self.alarmVar = 0
        
    def muteUnmuteSound(self):
        if self.flagMuteUnmuteSound == 0:
            self.effect1.setVolume(0)
            self.effect2.setVolume(0)
            self.effect3.setVolume(0)
            self.flagMuteUnmuteSound = 1
            self.btn_mute_unmute.setIcon(QIcon('Icons\mute-icon.png'))
            print(">>> Sound Muted")
        else:
            self.effect1.setVolume(0.75)
            self.effect2.setVolume(0.75)
            self.effect3.setVolume(0.75)
            self.flagMuteUnmuteSound = 0
            self.btn_mute_unmute.setIcon(QIcon("Icons\icons8-sound-48.png"))
            print(">>> Sound Unmuted")
        self.save_settings()
        
    def pausePlayProcess(self):
        # --------------------------------------------------------------------------------------------
        # pause and resume work
        if self.pauseResumeValue==0:
            if self.workIsStarted==1 and self.breakIsStarted==0 and self.longBreakIsStarted==0:
                remaining = int(self.Timer25min.remainingTime())
                self.Timer25min.stop();
                self.Timer25min.setInterval(remaining);
                self.pauseResumeValue=1
                self.btn_pause_play.setIcon(QIcon("icons\play-icon.png"))
        else:
            if self.workIsStarted==1 and self.breakIsStarted==0 and self.longBreakIsStarted==0:
                self.Timer25min.start(1000)
                self.pauseResumeValue=0
                self.btn_pause_play.setIcon(QIcon("icons\icons8-pause-48.png"))
        
        # --------------------------------------------------------------------------------------------
        # pause and resume break
        if self.pauseResumeValue==0:
            if self.workIsStarted==0 and self.breakIsStarted==1 and self.longBreakIsStarted==0:
                remaining = int(self.Timer25min.remainingTime())
                self.Timer5min.stop();
                self.Timer5min.setInterval(remaining);
                self.pauseResumeValue=1
                self.btn_pause_play.setIcon(QIcon("icons\play-icon.png"))
        else:
            if self.workIsStarted==0 and self.breakIsStarted==1 and self.longBreakIsStarted==0:
                self.Timer5min.start(1000)
                self.pauseResumeValue=0
                self.btn_pause_play.setIcon(QIcon("icons\icons8-pause-48.png"))
        
        # --------------------------------------------------------------------------------------------        
        # pause and resume long break
        if self.pauseResumeValue==0:
            if self.workIsStarted==0 and self.breakIsStarted==0 and self.longBreakIsStarted==1:
                remaining = int(self.Timer25min.remainingTime())
                self.Timer30min.stop();
                self.Timer30min.setInterval(remaining);
                self.pauseResumeValue=1
                self.btn_pause_play.setIcon(QIcon("icons\play-icon.png"))
        else:
            if self.workIsStarted==0 and self.breakIsStarted==0 and self.longBreakIsStarted==1:
                self.Timer30min.start(1000)
                self.pauseResumeValue=0
                self.btn_pause_play.setIcon(QIcon("icons\icons8-pause-48.png"))
                
                
    
    def cancel_process(self):
        # check if process mode is Auto set buttons & actions to -> disabled
        if self.process_combobox.currentIndex() == 0:
            self.btn_break.setEnabled(False)
            self.btn_long_break.setEnabled(False)
            self.tray_break_action.setEnabled(False)
            self.tray_long_break_action.setEnabled(False)
        # check if process mode is Single Shot set buttons & actions to -> enabled
        if self.process_combobox.currentIndex() == 1:
            self.btn_break.setEnabled(True)
            self.btn_long_break.setEnabled(True)
            self.tray_break_action.setEnabled(True)
            self.tray_long_break_action.setEnabled(True)

        # enable all buttons
        self.btn_start.setEnabled(True)
        #self.btn_quit.setEnabled(True)
        self.btn_reset.setEnabled(True)
        self.btn_clock.setEnabled(True)
        
        # enable actions
        self.tray_start_action.setEnabled(True)
        
        # enable all spin boxs
        self.work_spinbox.setEnabled(True)
        self.break_spinbox.setEnabled(True)
        self.long_break_spinbox.setEnabled(True)
        
        # set information label
        #self.information_label.setText("Ready")
        self.myStatusBar.showMessage("Ready")
        self.myStatusBar.showMessage(str(self.myStatusBar.currentMessage()) + " - Last Loop:" + str(self.count_work_user))
        
        # stop sound
        self.effect1.stop()
        self.effect2.stop()
        self.effect3.stop()
        
        # stop all timers
        self.Timer25min.stop()
        self.Timer5min.stop()
        self.Timer30min.stop()
        
        # set the labels text
        if self.work_spinbox.value() > 10:
            self.min_label.setText(str(self.work_spinbox.value()))
            self.min_lcd_number.display(str(self.work_spinbox.value()))
        if self.work_spinbox.value() < 9:
            self.min_label.setText("0" + str(self.work_spinbox.value()))
            self.min_lcd_number.display("0" + str(self.work_spinbox.value()))
        if self.work_spinbox.value() == 10:
            self.min_label.setText(str(self.work_spinbox.value()))
            self.min_lcd_number.display(str(self.work_spinbox.value()))
        if self.work_spinbox.value() == 9:
            self.min_label.setText("0" + str(self.work_spinbox.value()))
            self.min_lcd_number.display("0" + str(self.work_spinbox.value()))
        self.sec_label.setText("00")
        self.sec_lcd_number.display("00")
        
        # disable cancel button and action
        self.btn_cancel.setEnabled(False)
        self.tray_cancel_process.setEnabled(False)
        
        # stop alarm notification
        self.alarmNotificationStop()
        
        # set progress bar
        self.myProgressBar.setValue(0)
        self.myProgressBar.setFormat('')
        
        # disable pause play button
        self.btn_pause_play.setEnabled(False)
        self.btn_pause_play.setIcon(QIcon("icons\icons8-pause-48.png"))
        
        # change buttons color
        self.btn_start.setStyleSheet('background-color:rgb(63, 186, 41);')
        self.btn_cancel.setStyleSheet('background-color:rgb();')
        if self.process_combobox.currentText() == "Single Shot":
            self.btn_break.setStyleSheet('background-color:rgb(63, 186, 41);')
            self.btn_long_break.setStyleSheet('background-color:rgb(63, 186, 41);')
        else:
            self.btn_break.setStyleSheet('background-color:rgb();')
            self.btn_long_break.setStyleSheet('background-color:rgb();')
        
        # disable combobox
        self.process_combobox.setEnabled(True)
        
        # set program value -> not working (you not run any process)
        self.workIsStarted = 0
        self.breakIsStarted = 0
        self.longBreakIsStarted = 0
        self.count_work = 0
        self.count_work_user = 0

    def show_info(self):
        # open dialog
        self.information_dialog.exec()



myApp = QApplication(sys.argv)
window = LolikWindow(myApp)
window.show()
sys.exit(myApp.exec())
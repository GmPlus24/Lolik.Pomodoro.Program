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


#----------------------------------------------------------------------------------------------------------------------------------
def start_work_TimerCallBack(self):
    print(">>>  work__start_timer")
    
    
    
    if self.var_start_timer > 0 :
        self.var_start_timer -= 1
        
        if (int(self.work_spinbox.value()) - int(self.min_label.text())) < (int(self.work_spinbox.value()) / 2):
            self.myProgressBar.setValue(int(  ( (100 *   ( ( int(self.work_spinbox.value()) - int(self.min_label.text())) - 1 ) )     / int(self.work_spinbox.value()) ) ) )

        else:
            self.myProgressBar.setValue(int(  ( (100 *    ( int(self.work_spinbox.value()) - int(self.min_label.text()) ) )     / int(self.work_spinbox.value()) ) ) )

    if self.var_start_timer == 0:
        self.Timer25min.stop()
        self.workIsStarted = 0
        self.count_work += 1
        self.count_work_user += 1
        self.myProgressBar.setValue(0)
        
        # disable combobox
        if self.process_combobox.currentText() == "Single Shot":
            self.process_combobox.setEnabled(True)
        
        # change buttons color
        self.btn_start.setStyleSheet('background-color:rgb(63, 186, 41);')
        self.btn_cancel.setStyleSheet('background-color:rgb();')
        if self.process_combobox.currentText() == "Single Shot":
            self.btn_break.setStyleSheet('background-color:rgb(63, 186, 41);')
            self.btn_long_break.setStyleSheet('background-color:rgb(63, 186, 41);')
        else:
            self.btn_break.setStyleSheet('background-color:rgb();')
            self.btn_long_break.setStyleSheet('background-color:rgb();')

        # set label to 00:00
        self.min_label.setText("00")
        self.sec_label.setText("00")
        self.min_lcd_number.display("00")
        self.sec_lcd_number.display("00")
        
        # set progress bar
        self.myProgressBar.setFormat('')
        
               
        # start alarm notification timer
        self.TimerAlarmNotification.start()
        QTimer.singleShot(20000, self.alarmNotificationStop)
        
        # disable pause play button
        self.btn_pause_play.setEnabled(False)
        
        
 
        if self.count_work == 3:
            # set information label
            #self.information_label.setText("Waiting...")
            self.myStatusBar.showMessage("Waiting...")



            # play sound
            self.effect1.play()
            

            # show message box
            if self.message_box_check == "CHECK":
                self.ProcessFinishedDialog.setWindowTitle("Great Job!")
                
                self.myText.setText("\n\nYou work 3 times! Take a long break,\n click the long break button.")
                
                self.myTextInfo.setText("You can break: " + self.long_break_spinbox.text() + "\n" + "Get back to work: " + str(( datetime.now() + timedelta(minutes =  int(self.long_break_spinbox.value())  )).strftime('%H:%M')))
                
                # close message box
                QTimer.singleShot(self.time_milliseconds, lambda : self.ProcessFinishedDialog.accept())
                
                self.myTextInfo3.setText("20")
                self.StartDialogTimer()
                
                self.ProcessFinishedDialog.exec()
            
                # stop sound
                self.effect1.stop()
            
            
            
            
            if self.process_combobox.currentText() == "Single Shot":
                # enable all buttons
                self.btn_start.setEnabled(True)
                self.btn_long_break.setEnabled(True)
                #self.btn_quit.setEnabled(True)
                self.btn_break.setEnabled(True)
                self.btn_reset.setEnabled(True)
                self.btn_clock.setEnabled(True)
                
                # enable actions
                self.tray_start_action.setEnabled(True)
                self.tray_break_action.setEnabled(True)
                self.tray_long_break_action.setEnabled(True)
                
                # enable spin boxs
                self.work_spinbox.setEnabled(True)
                self.break_spinbox.setEnabled(True)
                self.long_break_spinbox.setEnabled(True)
                

                
                
            
            
            # set status bar
            self.myStatusBar.showMessage("Choose Process")
            
            print(self.process_mode)
            if self.process_mode == "AUTO - CONTINUOUS":
                QTimer.singleShot(1000, self._long_break_work)
                self.myStatusBar.showMessage(str(self.myStatusBar.currentMessage()) + " - Loop:" + str(self.count_work_user))
                            
            
            
            
        elif self.count_work < 3:
            # set information label
            #self.information_label.setText("Waiting...")
            self.myStatusBar.showMessage("Waiting...")
        
                  
            
            # play sound
            self.effect1.play()

            # show message box
            if self.message_box_check == "CHECK":
            
                self.ProcessFinishedDialog.setWindowTitle("Good Job!")
                
                self.myText.setText("\n\nYour work time is overed. Take a break,\n click the break button.")
                
                self.myTextInfo.setText("You can break: " + self.break_spinbox.text() + "\n" + "Get back to work: " + str(( datetime.now() + timedelta(minutes =  int(self.break_spinbox.value())  )).strftime('%H:%M')))
                
                # close message box
                QTimer.singleShot(self.time_milliseconds, lambda : self.ProcessFinishedDialog.accept())
                self.myTextInfo3.setText("20")
                self.StartDialogTimer()
                
                self.ProcessFinishedDialog.exec()
                # stop sound
                self.effect1.stop()
                
                
            if self.process_combobox.currentText() == "Single Shot":
                # enable all buttons
                self.btn_start.setEnabled(True)
                self.btn_long_break.setEnabled(True)
                #self.btn_quit.setEnabled(True)
                self.btn_break.setEnabled(True)
                self.btn_reset.setEnabled(True)
                self.btn_clock.setEnabled(True)
                
                # enable actions
                self.tray_start_action.setEnabled(True)
                self.tray_break_action.setEnabled(True)
                self.tray_long_break_action.setEnabled(True)
                
                # enable spin boxs
                self.work_spinbox.setEnabled(True)
                self.break_spinbox.setEnabled(True)
                self.long_break_spinbox.setEnabled(True)
                
            
            
            # set status bar
            self.myStatusBar.showMessage("Choose Process")
            
            if self.process_mode == "AUTO - CONTINUOUS":
                print("     aouto mode :/S/")
                QTimer.singleShot(1000, self._break_work)
                self.myStatusBar.showMessage(str(self.myStatusBar.currentMessage()) + " - Loop:" + str(self.count_work_user))


                            
        elif self.count_work > 3:
            # set information label
            #self.information_label.setText("Waiting...")
            self.myStatusBar.showMessage("Waiting...")
        

            # play sound
            self.effect1.play()

            # show message box
            if self.message_box_check == "CHECK":
            
                self.ProcessFinishedDialog.setWindowTitle("Great Job!")
                
                self.myText.setText("\n\nYour work too many times. Take a long break,\n click the long break button.")
                
                self.myTextInfo.setText("You can break: " + self.long_break_spinbox.text() + "\n" + "Get back to work: " + str(( datetime.now() + timedelta(minutes =  int(self.long_break_spinbox.value())  )).strftime('%H:%M')))
                
                # close message box
                QTimer.singleShot(self.time_milliseconds, lambda : self.ProcessFinishedDialog.accept())
                
                self.myTextInfo3.setText("20")
                self.StartDialogTimer()
                
                self.ProcessFinishedDialog.exec()
                
                # stop sound
                self.effect1.stop()
                
            
            if self.process_combobox.currentText() == "Single Shot":
                # enable all buttons
                self.btn_start.setEnabled(True)
                self.btn_long_break.setEnabled(True)
                #self.btn_quit.setEnabled(True)
                self.btn_break.setEnabled(True)
                self.btn_reset.setEnabled(True)
                self.btn_clock.setEnabled(True)
                
                # enable actions
                self.tray_start_action.setEnabled(True)
                self.tray_break_action.setEnabled(True)
                self.tray_long_break_action.setEnabled(True)
                
                # enable spin boxs
                self.work_spinbox.setEnabled(True)
                self.break_spinbox.setEnabled(True)
                self.long_break_spinbox.setEnabled(True)
            
                
            # set status bar
            self.myStatusBar.showMessage("Choose Process")
                
            if self.process_mode == "AUTO - CONTINUOUS":
                QTimer.singleShot(1000, self._long_break_work)
                self.myStatusBar.showMessage(str(self.myStatusBar.currentMessage()) + " - Loop:" + str(self.count_work_user))
                
                
                
    #print("var_start_timer: ", self.var_start_timer)

    # common block to display minutes
    # and seconds on GUI
    minutes, seconds = divmod(self.var_start_timer, 60)
    self.min_var = (f"{minutes:02d}")
    self.sec_var = (f"{seconds:02d}")

    self.min_label.setText(self.min_var)
    self.sec_label.setText(self.sec_var)
    self.min_lcd_number.display(self.min_var)
    self.sec_lcd_number.display(self.sec_var)


def _start_work(self):
    print(">>> button start clicked")
    
    # stop all timers
    self.Timer25min.stop()
    self.Timer5min.stop()
    self.Timer30min.stop()
  
    # enable cancel button and action
    self.btn_cancel.setEnabled(True)
    self.tray_cancel_process.setEnabled(True)
    
    # set information label
    #self.information_label.setText("Work Started")
    self.myStatusBar.showMessage("Work Started")
    self.myStatusBar.showMessage(str(self.myStatusBar.currentMessage()) + " - Loop:" + str(self.count_work_user))

    # disable buttons
    self.btn_start.setEnabled(False)
    self.btn_break.setEnabled(False)
    self.btn_long_break.setEnabled(False)
    #self.btn_quit.setEnabled(False)
    self.btn_reset.setEnabled(False)
    self.btn_clock.setEnabled(False)
    
    # disable actions
    self.tray_start_action.setEnabled(False)
    self.tray_break_action.setEnabled(False)
    self.tray_long_break_action.setEnabled(False)
    
    # disable spin boxs
    self.work_spinbox.setEnabled(False)
    self.break_spinbox.setEnabled(False)
    self.long_break_spinbox.setEnabled(False)
    
    # enable pause play button
    self.btn_pause_play.setEnabled(True)
    
    # set progress bar
    self.myProgressBar.setFormat('%p%  Done')
    
    # disable combobox
    self.process_combobox.setEnabled(False)
    
    # change buttons color
    self.btn_start.setStyleSheet('background-color:rgb(63, 186, 41);')
    self.btn_cancel.setStyleSheet('background-color:rgb(250, 15, 38);')
    self.btn_break.setStyleSheet('background-color:rgb();')
    self.btn_long_break.setStyleSheet('background-color:rgb();')
    
    # start 25 minute timer
    self.var_start_timer = self.work_spinbox.value() * 60
    self.Timer25min.start()
    self.workIsStarted = 1





#----------------------------------------------------------------------------------------------------------------------------------
def start_break_TimerCallBack(self):
    #print("start_break_TimerCallBack")

    if self.var_break_timer > 0:
        self.var_break_timer -= 1
        
        if (int(self.break_spinbox.value()) - int(self.min_label.text())) < (int(self.break_spinbox.value()) / 2):
            self.myProgressBar.setValue(int(  ( (100 *   ( ( int(self.break_spinbox.value()) - int(self.min_label.text())) - 1 ) )     / int(self.break_spinbox.value()) ) ) )

        else:
            self.myProgressBar.setValue(int(  ( (100 *    ( int(self.break_spinbox.value()) - int(self.min_label.text()) ) )     / int(self.break_spinbox.value()) ) ) )


    if self.var_break_timer == 0:
        self.Timer5min.stop()
        self.breakIsStarted = 0
        self.myProgressBar.setValue(0)

        # set label to 00:00
        self.min_label.setText("00")
        self.sec_label.setText("00")
        self.min_lcd_number.display("00")
        self.sec_lcd_number.display("00")
        
        # change buttons color
        self.btn_start.setStyleSheet('background-color:rgb(63, 186, 41);')
        self.btn_cancel.setStyleSheet('background-color:rgb();')
        if self.process_combobox.currentText() == "Single Shot":
            self.btn_break.setStyleSheet('background-color:rgb(63, 186, 41);')
            self.btn_long_break.setStyleSheet('background-color:rgb(63, 186, 41);')
        else:
            self.btn_break.setStyleSheet('background-color:rgb();')
            self.btn_long_break.setStyleSheet('background-color:rgb();')
        
        # set progress bar
        self.myProgressBar.setFormat('')
        
        # disable pause play button
        self.btn_pause_play.setEnabled(False)
        
        # disable combobox
        self.process_combobox.setEnabled(True)
        
        
        # set information label
        #self.information_label.setText("Waiting...")
        self.myStatusBar.showMessage("Waiting...")
        
        # play sound
        self.effect2.play()

        
        # show message box
        if self.message_box_check == "CHECK":
            
            self.ProcessFinishedDialog.setWindowTitle("Times Up!")
            
            self.myText.setText("\n\nYour break time is overed. Get back to work,\n click the start button.")
            
            self.myTextInfo.setText("You have to work: " + self.work_spinbox.text() + "\n" + "You can get back to break: " + str((datetime.now() + timedelta(minutes=int(self.work_spinbox.value()))).strftime('%H:%M')))
            
            # close message box
            QTimer.singleShot(self.time_milliseconds, lambda : self.ProcessFinishedDialog.accept())
            
            self.myTextInfo3.setText("20")
            self.StartDialogTimer()
            
            self.ProcessFinishedDialog.exec()
        
            # stop sound
            self.effect2.stop()
            
        
        if self.process_combobox.currentText() == "Single Shot":
                # enable all buttons
                self.btn_start.setEnabled(True)
                self.btn_long_break.setEnabled(True)
                #self.btn_quit.setEnabled(True)
                self.btn_break.setEnabled(True)
                self.btn_reset.setEnabled(True)
                self.btn_clock.setEnabled(True)
                
                # enable actions
                self.tray_start_action.setEnabled(True)
                self.tray_break_action.setEnabled(True)
                self.tray_long_break_action.setEnabled(True)
                
                # enable spin boxs
                self.work_spinbox.setEnabled(True)
                self.break_spinbox.setEnabled(True)
                self.long_break_spinbox.setEnabled(True)
        

        # set status bar
        self.myStatusBar.showMessage("Choose Process")
        
        if self.process_mode == "AUTO - CONTINUOUS":
            QTimer.singleShot(1000, self._start_work)
            self.myStatusBar.showMessage(str(self.myStatusBar.currentMessage()) + " - Loop:" + str(self.count_work_user))


    minutes, seconds = divmod(self.var_break_timer, 60)
    self.min_var = (f"{minutes:02d}")
    self.sec_var = (f"{seconds:02d}")
    
    self.min_label.setText(self.min_var)
    self.sec_label.setText(self.sec_var)
    self.min_lcd_number.display(self.min_var)
    self.sec_lcd_number.display(self.sec_var)

def _break_work(self):
    print(">>> button break clicked")
    
    # stop all timers
    self.Timer25min.stop()
    self.Timer5min.stop()
    self.Timer30min.stop()
    
    # enable cancel button and action
    self.btn_cancel.setEnabled(True)
    self.tray_cancel_process.setEnabled(True)
   
    # set information label
    #self.information_label.setText("Break Started")
    self.myStatusBar.showMessage("Break Started")
    self.myStatusBar.showMessage(str(self.myStatusBar.currentMessage()) + " - Loop:" + str(self.count_work_user))

    # disable buttons
    self.btn_start.setEnabled(False)
    self.btn_break.setEnabled(False)
    self.btn_long_break.setEnabled(False)
    #self.btn_quit.setEnabled(False)
    self.btn_reset.setEnabled(False)
    self.btn_clock.setEnabled(False)
    
    # disable actions
    self.tray_start_action.setEnabled(False)
    self.tray_break_action.setEnabled(False)
    self.tray_long_break_action.setEnabled(False)
    
    # disable spin boxs
    self.work_spinbox.setEnabled(False)
    self.break_spinbox.setEnabled(False)
    self.long_break_spinbox.setEnabled(False)
    
    # enable pause play button
    self.btn_pause_play.setEnabled(True)
    
    # set progress bar
    self.myProgressBar.setFormat('%p%  Done')
    
    # disable combobox
    self.process_combobox.setEnabled(False)
    
    # change buttons color
    self.btn_start.setStyleSheet('background-color:rgb();')
    self.btn_cancel.setStyleSheet('background-color:rgb(250, 15, 38);')
    self.btn_break.setStyleSheet('background-color:rgb(63, 186, 41);')
    self.btn_long_break.setStyleSheet('background-color:rgb();')
    
    # start 5 minute timer
    self.var_break_timer = self.break_spinbox.value() * 60
    self.Timer5min.start()
    self.breakIsStarted = 1
    
    
    
    
#----------------------------------------------------------------------------------------------------------------------------------
def start_long_break_TimerCallBack(self):
    #print("start_long_break_TimerCallBack")

    if self.var_long_break_timer > 0:
        self.var_long_break_timer -= 1
        print("if self.var_long_break_timer > 0:")
        print(self.var_long_break_timer)
        
        
        if (int(self.long_break_spinbox.value()) - int(self.min_label.text())) < (int(self.long_break_spinbox.value()) / 2):
            self.myProgressBar.setValue(int(  ( (100 *   ( ( int(self.long_break_spinbox.value()) - int(self.min_label.text())) - 1 ) )     / int(self.long_break_spinbox.value()) ) ) )

        else:
            self.myProgressBar.setValue(int(  ( (100 *    ( int(self.long_break_spinbox.value()) - int(self.min_label.text()) ) )     / int(self.long_break_spinbox.value()) ) ) )
           

    if self.var_long_break_timer == 0:
        print("if self.var_long_break_timer == 0:")
        self.Timer30min.stop()
        self.longBreakIsStarted = 0
        
        # change buttons color
        self.btn_start.setStyleSheet('background-color:rgb(63, 186, 41);')
        self.btn_cancel.setStyleSheet('background-color:rgb();')
        if self.process_combobox.currentText() == "Single Shot":
            self.btn_break.setStyleSheet('background-color:rgb(63, 186, 41);')
            self.btn_long_break.setStyleSheet('background-color:rgb(63, 186, 41);')
        else:
            self.btn_break.setStyleSheet('background-color:rgb();')
            self.btn_long_break.setStyleSheet('background-color:rgb();')

        # set label to 00:00
        self.min_label.setText("00")
        self.sec_label.setText("00")
        self.min_lcd_number.display("00")
        self.sec_lcd_number.display("00")
        
        # set progress bar
        self.myProgressBar.setFormat('')
        
        # disable pause play button
        self.btn_pause_play.setEnabled(False)
        
        # disable combobox
        self.process_combobox.setEnabled(True)
        
        
        # set information label
        #self.information_label.setText("Waiting...")
        self.myStatusBar.showMessage("Waiting...")
        
        # play sound
        self.effect3.play()

        
        if self.message_box_check == "CHECK":
        
            self.ProcessFinishedDialog.setWindowTitle("Times Up!")
            
            self.myText.setText("\n\nYour long break time is overed. Get back to work,\n click the start button.")
            
            self.myTextInfo.setText("You have to work: " + self.work_spinbox.text() + "\n" + "You can get back to break: " + str((datetime.now() + timedelta(minutes=int(self.work_spinbox.value()))).strftime('%H:%M')))
            
            # close message box
            QTimer.singleShot(self.time_milliseconds, lambda : self.ProcessFinishedDialog.accept())
            
            self.myTextInfo3.setText("20")
            self.StartDialogTimer()
            
            self.ProcessFinishedDialog.exec()
        
            # stop sound
            self.effect3.stop()
            
        
        if self.process_combobox.currentText() == "Single Shot":
            # enable all buttons
            self.btn_start.setEnabled(True)
            self.btn_long_break.setEnabled(True)
            #self.btn_quit.setEnabled(True)
            self.btn_break.setEnabled(True)
            self.btn_reset.setEnabled(True)
            self.btn_clock.setEnabled(True)
            
            # enable actions
            self.tray_start_action.setEnabled(True)
            self.tray_break_action.setEnabled(True)
            self.tray_long_break_action.setEnabled(True)
            
            # enable spin boxs
            self.work_spinbox.setEnabled(True)
            self.break_spinbox.setEnabled(True)
            self.long_break_spinbox.setEnabled(True)
        
        
        # set status bar
        self.myStatusBar.showMessage("Choose Process")
        
        if self.process_mode == "AUTO - CONTINUOUS":
            QTimer.singleShot(1000, self._start_work)
            self.myStatusBar.showMessage(str(self.myStatusBar.currentMessage()) + " - Loop:" + str(self.count_work_user))

        
        # set count_work variable to 0
        self.count_work = 0
    
    
    minutes, seconds = divmod(self.var_long_break_timer, 60)
    self.min_var = (f"{minutes:02d}")
    self.sec_var = (f"{seconds:02d}")
    
    self.min_label.setText(self.min_var)
    self.sec_label.setText(self.sec_var)
    self.min_lcd_number.display(self.min_var)
    self.sec_lcd_number.display(self.sec_var)




def _long_break_work(self):
    print(">>> button long break clicked")

    # stop all timers
    self.Timer25min.stop()
    self.Timer5min.stop()
    self.Timer30min.stop()
    
    # enable cancel button and action
    self.btn_cancel.setEnabled(True)
    self.tray_cancel_process.setEnabled(True)
    
    # set information label
    #self.information_label.setText("Long Break Started")
    self.myStatusBar.showMessage("Long Break Started")
    self.myStatusBar.showMessage(str(self.myStatusBar.currentMessage()) + " - Loop:" + str(self.count_work_user))

    # disable buttons
    self.btn_start.setEnabled(False)
    self.btn_break.setEnabled(False)
    self.btn_long_break.setEnabled(False)
    #self.btn_quit.setEnabled(False)
    self.btn_reset.setEnabled(False)
    self.btn_clock.setEnabled(False)
    
    # disable actions
    self.tray_start_action.setEnabled(False)
    self.tray_break_action.setEnabled(False)
    self.tray_long_break_action.setEnabled(False)
    
    
    # disable spin boxs
    self.work_spinbox.setEnabled(False)
    self.break_spinbox.setEnabled(False)
    self.long_break_spinbox.setEnabled(False)
    
    # enable pause play button
    self.btn_pause_play.setEnabled(True)
    
    # set progress bar
    self.myProgressBar.setFormat('%p%  Done')
    
    # disable combobox
    self.process_combobox.setEnabled(False)
    
    # change buttons color
    # change buttons color
    self.btn_start.setStyleSheet('background-color:rgb();')
    self.btn_cancel.setStyleSheet('background-color:rgb(250, 15, 38);')
    self.btn_break.setStyleSheet('background-color:rgb();')
    self.btn_long_break.setStyleSheet('background-color:rgb(63, 186, 41);')
    
    # start 30 minute timer
    self.var_long_break_timer = self.long_break_spinbox.value() * 60
    self.Timer30min.start()
    self.longBreakIsStarted = 1
    
    
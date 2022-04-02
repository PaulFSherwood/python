#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from pprint import pprint
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QInputDialog, QLineEdit, 
                             QMessageBox, QPushButton, QToolTip, QWidget)

class PasswordSaver(QWidget):
    # initialize
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    # 1
    #####
    
    def initUI(self):
        
        #####
        # 1
        self.setGeometry(300, 300, 300, 220)
        #####
        # 5
        self.center()
        # 5
        #####
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('images/web.png'))
        #
        ##########
        # BUTTONS
        self.btn = QPushButton('Open', self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)
        
        self.text_name = QLineEdit(self)
        self.text_name.move(100,22)
        self.text_name.setPlaceholderText("enter your name")
        # buttons
        ##########
        self.show()
        # 1
        #####
    #####
    # 4
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "You wish to quit?", 
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        if (reply == QMessageBox.Yes):
            event.accept()
        else:
            event.ignore()
    # 4
    #####
    #####
    # 5
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    # 5
    #####
    def LookupPass(self):
        # shoot open a pop up and get the password?
        text, ok = self.QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
    #####
    # trying out clicked event for show messge update
    def updateShowMessage(self):
        text, ok = self.QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
    
    def showDialog(self):
        text, result = QInputDialog.getText(self, 'Input Dialog', 'Enter Your name:')
        print("text:", text)
        if result == True:
            self.text_name.setText(str(text))
            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    
    ex = PasswordSaver()
    sys.exit(app.exec_())
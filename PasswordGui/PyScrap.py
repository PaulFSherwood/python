##!/usr/bin/python3
## -*- coding: utf-8 -*-
#
#"""
#ZetCode PyQt5 tutorial 
#
#In this example, we receive data from
#a QInputDialog dialog. 
#
#author: Jan Bodnar
#website: zetcode.com 
#last edited: January 2015
#"""
#
#import sys
#from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
#    QInputDialog, QApplication, QMainWindow)
#
#
#class Example(QWidget):
#    
#    def __init__(self):
#        super().__init__()
#        
#        self.initUI()
#        
#        
#    def initUI(self):      
#
#        self.btn = QPushButton('Dialog', self)
#        self.btn.move(20, 20)
#        self.btn.clicked.connect(self.showDialog)
#        
#        self.le = QLineEdit(self)
#        self.le.move(130, 22)
#        
#        self.setGeometry(300, 300, 290, 150)
#        self.setWindowTitle('Input dialog')
#        self.show()
#        
#        
#    def showDialog(self):
#        
#        text, ok = QInputDialog.getText(self, 'Input Dialog', 
#            'Enter your name:')
#        
#        if ok:
#            self.le.setText(str(text))
#        
#        
#if __name__ == '__main__':
#    
#    app = QApplication(sys.argv)
#    ex = Example()
#    sys.exit(app.exec_())
    
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 10
        self.top = 30
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
 
        self.show()
 
class MyTableWidget(QWidget):        
 
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
# 
#        # Initialize tab screen
#        self.tabs = QTabWidget()
#        self.tab1 = QWidget()	
#        self.tab2 = QWidget()
#        self.tabs.resize(300,200) 
# 
#        # Add tabs
#        self.tabs.addTab(self.tab1,"Tab 1")
#        self.tabs.addTab(self.tab2,"Tab 2")
# 
#        # Create first tab
#        self.tab1.layout = QVBoxLayout(self)
#        self.pushButton1 = QPushButton("PyQt5 button")
#        self.tab1.layout.addWidget(self.pushButton1)
#        self.tab1.setLayout(self.tab1.layout)
# 
#        # Add tabs to widget        
#        self.layout.addWidget(self.tabs)
#        self.setLayout(self.layout)
# 
#    @pyqtSlot()
#    def on_click(self):
#        print("\n")
#        for currentQTableWidgetItem in self.tableWidget.selectedItems():
#            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
# 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
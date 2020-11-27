# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PasswordGui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QInputDialog

#The password list - We start with it populated for testing purposes
passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"], ["aaa", "aaabbb"]]

#The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

#The encryption key for the caesar cypher
encryptionKey=16

def passwordEncrypt (unencryptedMessage, key):
    #We will start with an empty string as our encryptedMessage
    encryptedMessage = ''
    #For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'): 
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return str(encryptedMessage)

def loadPasswordFile(fileName):
    try:
        f = open(fileName, 'rb')
    except IOError:
        print("could not load file", fileName)
        sys.exit()
    with open(fileName, 'r', encoding='utf-8', newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)
    
    return passwordList

def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', encoding='utf-8', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)

class Ui_Form(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.OpenPasswordBtn = QtWidgets.QPushButton(Form)
        self.OpenPasswordBtn.setObjectName("OpenPasswordBtn")
        self.verticalLayout.addWidget(self.OpenPasswordBtn)
        self.LookupPasswordBtn = QtWidgets.QPushButton(Form)
        self.LookupPasswordBtn.setObjectName("LookupPasswordBtn")
        self.verticalLayout.addWidget(self.LookupPasswordBtn)
        self.AddPasswordBtn = QtWidgets.QPushButton(Form)
        self.AddPasswordBtn.setObjectName("AddPasswordBtn")
        self.verticalLayout.addWidget(self.AddPasswordBtn)
        self.DeletePasswordBtn = QtWidgets.QPushButton(Form)
        self.DeletePasswordBtn.setObjectName("DeletePasswordBtn")
        self.verticalLayout.addWidget(self.DeletePasswordBtn)
        self.ChangePasswordBtn = QtWidgets.QPushButton(Form)
        self.ChangePasswordBtn.setObjectName("ChangePasswordBtn")
        self.verticalLayout.addWidget(self.ChangePasswordBtn)
        self.SavePasswordBtn = QtWidgets.QPushButton(Form)
        self.SavePasswordBtn.setObjectName("SavePasswordBtn")
        self.verticalLayout.addWidget(self.SavePasswordBtn)
        self.ShowAllPasswordBtn = QtWidgets.QPushButton(Form)
        self.ShowAllPasswordBtn.setObjectName("ShowAllPasswordBtn")
        self.verticalLayout.addWidget(self.ShowAllPasswordBtn)      
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Password Saver"))
        self.OpenPasswordBtn.setText(_translate("Form", "Open"))
        self.LookupPasswordBtn.setText(_translate("Form", "Lookup"))
        self.AddPasswordBtn.setText(_translate("Form", "Add"))
        self.DeletePasswordBtn.setText(_translate("Form", "Delete"))
        self.ChangePasswordBtn.setText(_translate("Form", "Change"))
        self.SavePasswordBtn.setText(_translate("Form", "Save"))
        self.ShowAllPasswordBtn.setText(_translate("Form", "Show Passwords"))
        # add actions for buttons / event triggers for functions calls
        self.OpenPasswordBtn.clicked.connect(self.OpenPassFile) # 1 - Done
        self.LookupPasswordBtn.clicked.connect(self.LookupPass) # 2 - Done
        self.AddPasswordBtn.clicked.connect(self.addWebsite)    # 3 - Done
        self.DeletePasswordBtn.clicked.connect(self.DeletePass) # 4 - Done
        self.ChangePasswordBtn.clicked.connect(self.ChangePass) # 5 - Done
        self.SavePasswordBtn.clicked.connect(self.SavePass)     # 6 - Done
        self.ShowAllPasswordBtn.clicked.connect(self.ShowPass)  # 7 - Done
                                                                # 8 - Taken care of by the X
    
    #####
    # 1 - OPEN a file and load it
    def OpenPassFile(self):
        # Open and load the password file
        global passwords
        passwords = loadPasswordFile(passwordFileName)
        self.textEdit.setText("File loaded SUCCESS")
        for keyvalue in passwords:
            self.textEdit.append(keyvalue[0])
    #####
    # 2 - FIND a password
    def LookupPass(self):
        myString = ''
        for keyvalue in passwords:  # this is broken for sites with multiple passwords
            myString = myString + (keyvalue[0] + " ")
        # show the possibles in the window
        self.textEdit.setText(" ====================")
        self.textEdit.append("\tYour Sites")
        for keyvalue in passwords:
            self.textEdit.append(keyvalue[0])
        self.textEdit.append(" ====================")
        # shoot open a pop up and get the password?
        passwordToLookup, ok = QInputDialog.getText(self, 'Enter Website', 'Enter the website for the password:')
        
        # test the inputText against the passsword list
        for keyvalue in passwords:
            # if we find a match show the password
            if passwordToLookup == keyvalue[0]:
                self.textEdit.setText(" ====================")
                self.textEdit.append("\tYour Password\t")
                self.textEdit.append("\t" + passwordEncrypt(keyvalue[1], -(encryptionKey)))
                self.textEdit.append(" ====================")
                
    #####
    # 3 - ADD a password to the website
    def addWebsite(self):
        # get the site name that the user wants
        website, ok = QInputDialog.getText(self, 'Enter Website', 'Enter the NEW website:')
        # show the site
        self.textEdit.setText(website)
        # get the password
        unencryptedPassword, ok = QInputDialog.getText(self, 'Enter Password', 'Enter the site password:')
        # encrypt the new password
        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)
        self.textEdit.append("PASSWORD ACCEPTED")
        # create a size 2 list
        tempList = [website, encryptedPassword]
        # append the tempList to the password list
        passwords.append(tempList)
    
    #####
    # 4 - DELETE a website and password
    def DeletePass(self):
        # get the website
        userWebsite, ok = QInputDialog.getText(self, 'Enter Website', 'Enter the website to DELETE:')
        # update the user with info
        self.textEdit.setText("Thank you we have the website")
        self.textEdit.append(userWebsite)
        # get the password for the website from the user
        userPassword, ok = QInputDialog.getText(self, 'Enter Password', 'Enter the website Password:')
        # flip through the password list again (probably should have saved this meh, we got ram)
        for x, y in enumerate(passwords): # could have used (for i in passwords) again trying out enumerate
            if y[0] == userWebsite:
                if y[1] == passwordEncrypt(userPassword, encryptionKey):
                    # Delete the website and password from our list
                    passwords.remove([userWebsite, passwordEncrypt(userPassword, encryptionKey)])
                    self.textEdit.setText("We found and deleted the site and password")
        # removed showing the remaining sites
    
    #####
    # 5 - CHANGE the website password
    def ChangePass(self):
        # Get the website to change
        userWebsite, ok = QInputDialog.getText(self, 'Enter Website', 'Enter the website to CHANGE:')
        # get the curent password for the site
        userPassword, ok = QInputDialog.getText(self, 'Enter Password', 'Enter the website Password:')
        # flip through the password list again
        for x, y in enumerate(passwords):
            # verify the site and the password at the same time
            if (y[0] == userWebsite):
                print(y[1])
                if (y[1] == passwordEncrypt(userPassword, encryptionKey)):
                    # get the new password
                    newPassword, ok = QInputDialog.getText(self, 'Enter Password', 'Please enter the NEW site password:')
                    # update the the site with the new password
                    passwords.remove([userWebsite, passwordEncrypt(userPassword, encryptionKey)])
                    passwords.append([userWebsite, passwordEncrypt(newPassword, encryptionKey)])
                    self.textEdit.setText("We found and updated your site password")
                    self.textEdit.append("=======================================")
                    break

    #####
    # 6 - SAVE the websites and passwords
    def SavePass(self):
        # save the list to the password file
        savePasswordFile(passwords, passwordFileName)
        
    #####
    # 7 - SHOW the websites and passwords
    def ShowPass(self):
        self.textEdit.setText("==========================")
        self.textEdit.append("||\tYour Sites\t||")
        for keyvalue in passwords:
            self.textEdit.append(', '.join(keyvalue))
        self.textEdit.append("==========================")
        
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ex = Ui_Form()
    ex.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
        


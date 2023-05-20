# default main file and load user_interface.py
from PySide6 import QtCore, QtWidgets
from user_interface import UserInterface
import sys

app = QtWidgets.QApplication(sys.argv)
window = UserInterface()
window.show()
app.exec()
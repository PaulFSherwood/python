# default main file and load UI file
from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from icon_fix import * # fixes the icon issue
import qtawesome as qta # to access icons


loader = QUiLoader() # set up a loader object

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        # Load UI
        self.ui = loader.load("userdata.ui", None) # load the ui
        # Load QSS stylesheet
        self.style_file = QFile("style.qss")
        self.style_file.open(QFile.OpenMode.ReadOnly)
        self.style_sheet = str(self.style_file.readAll(), encoding='utf-8')
        self.style_file.close()
        # apply the stylesheet
        self.ui.setStyleSheet(self.style_sheet)
        # load and fix Icons
        self.ui.setWindowIcon(qta.icon("fa5s.praying-hands" , color='red'))  # add an window icon
        set_taskbar_icon() # fix the icon issue

        # connect signals
        self.ui.submit_button.clicked.connect(self.do_something)

    def show(self):
        self.ui.show()

    def do_something(self):
        print(self.ui.full_name_line_edit.text(), "is a", self.ui.occupation_line_edit.text())

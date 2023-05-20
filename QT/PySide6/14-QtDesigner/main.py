# default main file and load UI file
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from icon_fix import * # fixes the icon issue
import qtawesome as qta # to access icons
import sys

loader = QUiLoader() # set up a loader object

app = QApplication(sys.argv)
window = loader.load("userdata.ui", None) # load the ui - happens at runtime so no need to recompile
window.setWindowIcon(qta.icon("fa5s.praying-hands" , color='red'))  # add an window icon
set_taskbar_icon() # fix the icon issue

# load the stylesheet seperately
style_file = QFile("style.qss")
style_file.open(QFile.OpenMode.ReadOnly)
style_sheet = str(style_file.readAll(), encoding='utf-8')
style_file.close()

# apply the stylesheet
window.setStyleSheet(style_sheet)


def do_something():
    print(window.full_name_line_edit.text(), "is a ", window.occupation_line_edit.text())

# Changing the properties in the form
window.setWindowTitle("User Data")

# accessing widgets in the form
window.submit_button.clicked.connect(do_something)
window.show()
app.exec()
from PySide6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QTabWidget,
                               QPushButton, QLabel, QCheckBox, QRadioButton,
                               QLineEdit)
# from PySide6.QtGui import QFont
# import qtawesome as qta
# NOTE: If you want to see all available icons run the following command:
# qta-browser
# this will open a window and you can browse all the available icons.
import qtawesome as qta
# icon support
from PySide6.QtGui import QIcon
import ctypes, platform
# Setup to test for operating system version
os_name = platform.system()



class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # set widget minimum size
        self.setMinimumSize(300, 200)
        # set the windows icon to me.png
        # self.setWindowIcon(qta.icon("mdi.account"))
        # self.setWindowIcon(QIcon("images/me.png"))
        self.setWindowIcon(qta.icon("fa5s.praying-hands" , color='red'))

        # Icon fix so it displays correctly on Windows 10 taskbar
        if os_name == "Windows":
            # Taskbar Icon fix from: https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
            myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


        self.setWindowTitle("QTabWidget")

        tab_widget = QTabWidget(self)

        # Information
        widget_form = QWidget()
        label_full_name = QLabel("Full name :")
        self.line_edit_full_name = QLineEdit()
        form_layout = QVBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(self.line_edit_full_name)
        widget_form.setLayout(form_layout)

        # Buttons
        widget_buttons = QWidget()
        button_1 = QPushButton("One")
        button_1.clicked.connect(self.button_1_clicked)
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button_1)
        buttons_layout.addWidget(button_2)
        buttons_layout.addWidget(button_3)
        widget_buttons.setLayout(buttons_layout)

        # Add Tabs to widget
        tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_buttons, "Buttons")

        layout = QHBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

    def button_1_clicked(self):
        # show the text from 'line_edit_full_name'
        print("Button 1 clicked : ", self.line_edit_full_name.text())



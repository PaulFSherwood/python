from PySide6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                               QPushButton, QLabel, QComboBox )
# from PySide6.QtGui import QFont
# import qtawesome as qta
# NOTE: If you want to see all available icons run the following command:
# qta-browser
# this will open a window and you can browse all the available icons.
import qtawesome as qta
# icon support
from PySide6.QtGui import QIcon
from icon_fix import set_taskbar_icon


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # set widget minimum size
        self.setMinimumSize(300, 200)
        # set the window icon
        self.setWindowIcon(qta.icon("fa5s.praying-hands" , color='red'))

        set_taskbar_icon()  # Fix taskbar icon for Windows 10

        self.setWindowTitle("QTabWidget")

        # create a combo box
        self.combo_box = QComboBox(self)
        # add the nine planets to the combo box
        self.combo_box.addItems(["Mercury", "Venus", "Earth", "Mars", "Jupiter"])
        self.combo_box.addItem("Saturn")
        self.combo_box.addItem("Uranus")
        self.combo_box.addItem("Neptune")
        self.combo_box.addItem("Pluto")

        # add value buttons
        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.get_current_value)
        button_set_value = QPushButton("Set Value")
        button_set_value.clicked.connect(self.set_value)
        button_get_value = QPushButton("Get Value")
        button_get_value.clicked.connect(self.get_value)

        # create layout for combo box
        combo_box_layout = QHBoxLayout()
        combo_box_layout.addWidget(self.combo_box)
        combo_box_layout.addWidget(button_current_value)
        combo_box_layout.addWidget(button_set_value)
        combo_box_layout.addWidget(button_get_value)

        # add everything to the main layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_value)
        v_layout.addWidget(button_get_value)

        self.setLayout(v_layout)

    def get_current_value(self):
        print("Current item: ", self.combo_box.currentText(),
              " - current index: ", self.combo_box.currentIndex())

    def set_value(self):
        # self.combo_box.setCurrentText("Earth")
        self.combo_box.setCurrentIndex(2)
    
    def get_value(self):
        # print(self.combo_box.itemText(2))
        for i in range(self.combo_box.count()):
            print("index [ ", i, " ]: ", self.combo_box.itemText(i))

    
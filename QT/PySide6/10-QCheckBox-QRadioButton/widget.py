from PySide6.QtWidgets import (QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QGroupBox, 
                               QButtonGroup, QRadioButton)

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        # Set the title of the window
        self.setWindowTitle("QCheckBox and QRadioButton")
        # Set the size of the window
        self.setMinimumSize(400, 300)

        # Chekboxes : operating system
        os = QGroupBox("Choose operating system")

        # Create checkboxes for each operating system
        self.windows = QCheckBox("Windows")
        self.windows.toggled.connect(self.windows_box_toggled)
        self.linux = QCheckBox("Linux")
        self.linux.toggled.connect(self.linux_box_toggled)
        self.mac = QCheckBox("Mac")
        self.mac.toggled.connect(self.mac_box_toggled)
        
        # Create layout for checkboxes
        os_layout = QVBoxLayout()
        os_layout.addWidget(self.windows)
        os_layout.addWidget(self.linux)
        os_layout.addWidget(self.mac)

        # Apply layout to the groupbox
        os.setLayout(os_layout)

        # Exclusive checkboxes : Drinks
        drinks = QGroupBox("Choose your drink")
        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)

        # Make the checkboxes exclusive
        exclusive_button_group = QButtonGroup(self) # the self parent is needed here to avoid garbage collection of the button group object 
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffee)
        drinks.setLayout(drink_layout)

        # Radio buttons : answer
        answers = QGroupBox("Choose Answer")
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_a.setChecked(True)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)

        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)

        self.setLayout(v_layout)

    def windows_box_toggled(self, checked):
        if checked:
            print("Windows is checked")
            # Uncheck the other checkboxes (use exclusive checkboxes instead)
            # self.linux.setChecked(False)
            # self.mac.setChecked(False)
        else:
            print("Windows is unchecked")
    def linux_box_toggled(self, checked):
        if checked:
            print("Linux is checked")
            # Uncheck the other checkboxes (use exclusive checkboxes instead)
            # self.windows.setChecked(False)
            # self.mac.setChecked(False)
        else:
            print("Linux is unchecked")
    def mac_box_toggled(self, checked):
        if checked:
            print("Mac is checked")
            # Uncheck the other checkboxes (use exclusive checkboxes instead)
            # self.windows.setChecked(False)
            # self.linux.setChecked(False)
        else:
            print("Mac is unchecked")
# Importing the components we need
from PySide6.QtWidgets import QPushButton

# Building on top of QMainWindow
class ButtonHolder:
    def __init__(self):
        # super().__init__()

        # self.setWindowTitle("Button Holder")

        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)

        # Set our button as the central widget
        # self.setCentralWidget(button)

        # Connect the button to a function
        # button.clicked.connect(self.button_clicked)

    # Function to be called when the button is clicked
    def button_clicked(self, data):     # alternative to this would be adding self.
        print("You clikced : ", data)   # to all button related variables

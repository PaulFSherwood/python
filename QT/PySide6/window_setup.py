from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from button_holder import ButtonHolder
from slider_holder import SliderHolder

class WindowSetup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button and Slider Window")

        # Create instances of the button and slider classes
        button = QPushButton("Click Me")
        slider = MySlider()

        # Add the button and slider to the layout
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(slider)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

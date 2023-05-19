from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from button_holder import ButtonHolder
from slider_holder import SliderHolder

# setup WindowSetup class that should contain all other imported classes
class WindowSetup(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def setup(self):
        # create instances of ButtonHolder and SliderHolder
        self.button = ButtonHolder()
        self.slider = SliderHolder()
        # Additional components can be added here

        self.button.button.clicked.connect(self.button.button_clicked)
        self.slider.slider.valueChanged.connect(self.slider.slider_moved)
        # self.slider.slider_moved(44)
        # self.slider.slider.valueChanged.connect(self.slider_moved)

        # set layout box layout
        layout = QVBoxLayout()
        layout.addWidget(self.button.button)
        layout.addWidget(self.slider.slider)

        # Set the button and slider as the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        # self.setCentralWidget(self.slider.slider)




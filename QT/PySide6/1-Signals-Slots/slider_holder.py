from PySide6.QtWidgets import QSlider

class SliderHolder:
    def __init__(self, parent=None):
        # super().__init__(parent)
        self.slider = QSlider()

    # the slot : responds when something happens
    def slider_moved(self, data):
        print("Slider moved to : ", data)
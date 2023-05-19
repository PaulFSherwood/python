from PySide6.QtWidgets import QApplication, QSlider

class SliderHolder(QSlider):
    def __init__(self, parent=None):
        # super().__init__(parent)
        slider = QSlider()

    # the slot : responds when something happens
    def respond_to_slider(data):
        print("Slider moved to : ", data)
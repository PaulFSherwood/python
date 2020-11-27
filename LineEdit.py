import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # build a line edit widget
        # build a push button widget
        self.le = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Print')

        # set v_box as a VBox Layout
        # add the line edit to the layout
        # add the button to the layout
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)

        # set the current layout to our v_box layout
        self.setLayout(v_box)

        self.setWindowTitle('PyQt5 Lesson 8')

        self.show()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec())
import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):     # constructor
        super().__init__()  # parent class constructor

        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('Push IT')
        self.l = QtWidgets.QLabel('I have not been clicked yet')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Lesson 5')

        self.b.clicked.connect(self.btn_click)  # connect signal to a slot (run a function)

        self.show()

    def btn_click(self):    # button is click run this function
        self.l.setText('Ihave been clicked')


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

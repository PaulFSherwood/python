import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # stuff that should be on the screen
        self.lbl = QLabel('Which do you like best')
        self.dog = QRadioButton('Dogs')
        self.cat = QRadioButton('Cats')
        self.btn = QPushButton('Select')

        # how it should show up on the screen
        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.dog)
        layout.addWidget(self.cat)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Lesson 10')

        # event handling
        self.btn.clicked.connect(lambda: self.btn_clk(self.dog.isChecked(), self.cat.isChecked(), self.lbl))
        # window size
        self.setGeometry(100, 100, 300, 150)
        # show everhing/loop/
        self.show()

    def btn_clk(self, DogChk, CatChk, lbl):
        if DogChk:
            lbl.setText('I guess you like dogs')
        else:
            if CatChk:
                lbl.setText('So its cats for you')
            else:
                lbl.setText('Pick something already')

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
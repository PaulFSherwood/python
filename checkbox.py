import sys
from PyQt5.QtWidgets import (QLabel, QCheckBox, QPushButton, QVBoxLayout, QApplication, QWidget)

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel()
        self.lbl2 = QLabel()
        self.chx = QCheckBox('Do you like dogs?')
        self.btn = QPushButton("Push me")

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.lbl2)
        layout.addWidget(self.chx)
        layout.addWidget(self.btn)

        self.lbl2.setText("something")

        self.setLayout(layout)

        self.btn.clicked.connect(lambda: self.btn_clk(self.chx.isChecked(), self.lbl))
        self.show()

    def btn_clk(self, chk, lbl):
        if chk:
            lbl.setText('I guess you like dogs')
        else:
            lbl.setText("Dog hater then")

# application loop
app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
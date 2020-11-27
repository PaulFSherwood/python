import os
import sys # to exit the program
from pathlib import Path
                            # event loop  # look at  # window # buttons    # lay to put work
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        # what we want on the screen
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.sav_btn = QPushButton('Save')
        self.opn_btn = QPushButton('Open')

        self.init_ui()

    def init_ui(self):
        # where we want all our tings
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        # group buttons in a horizontal row
        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.sav_btn)
        h_layout.addWidget(self.opn_btn)

        # add text field to the layout
        v_layout.addWidget(self.text)
        # add the row of buttons to the layout
        v_layout.addLayout(h_layout)

        self.clr_btn.clicked.connect(self.clear_text)
        self.sav_btn.clicked.connect(self.save_text)
        self.opn_btn.clicked.connect(self.open_text)

        self.setLayout(v_layout)
        self.setWindowTitle('PyQt5 TextEdit')
        # show all the things
        self.show()

    # clear the text field
    def clear_text(self):
        self.text.clear()

    # open a file function
    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        # filename = QFileDialog.getSaveFileName(self, 'Save File', str(Path.home()))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)


    # open file
    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', str(Path.home()))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)


app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())
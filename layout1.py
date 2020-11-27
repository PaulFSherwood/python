import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton('Push Me')
    l = QtWidgets.QLabel('Look at me')
    
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()  #  take up room
    h_box.addWidget(l)  # put wid in the middle
    h_box.addStretch()  # take up room

    # build a layout
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    v_box.addLayout(h_box)  # add the horz. layout to the vert one
    # v_box.addWidget(l)
    w.setLayout(v_box)  # show this layout
    
    w.setWindowTitle('PyQt5 Lesson 4')
    w.show()
    
    sys.exit(app.exec_())
    
window()
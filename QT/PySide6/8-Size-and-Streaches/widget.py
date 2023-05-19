from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy, QPushButton, QLineEdit


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size policies and stretches")

        # Size policy : how the widgets behaves if container space is expanded or shrunk
        label = QLabel("Some text : ")
        line_edit = QLineEdit()
        # setSizePolicy: takes two arguments : horizontal and vertical
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)



        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        # Stretch : how muhc of the available space (in the layout) is occupied by the widget
        # You specify the stretch when you add things to the layout : button_1, 0, button_2, 1, button_3, 2
        # button_2 and button_3 each take up 1 unit

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1, 2)
        h_layout_2.addWidget(button_2, 1)
        h_layout_2.addWidget(button_3, 1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)


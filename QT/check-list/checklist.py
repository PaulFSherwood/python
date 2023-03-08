from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QCheckBox
import sys

class CheckListCreator(QWidget):
    def __init__(self):
        super().__init__()

        self.list_widget = QListWidget()
        self.checkbox1 = QCheckBox("Item 1")
        self.checkbox2 = QCheckBox("Item 2")
        self.checkbox3 = QCheckBox("Item 3")

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.checkbox3)

        self.setLayout(layout)

        self.checkbox1.stateChanged.connect(self.checkbox_changed)
        self.checkbox2.stateChanged.connect(self.checkbox_changed)
        self.checkbox3.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        sender = self.sender()
        if state == 2:
            self.list_widget.addItem(sender.text())
        else:
            items = self.list_widget.findItems(sender.text(), QtCore.Qt.MatchExactly)
            for item in items:
                self.list_widget.takeItem(self.list_widget.row(item))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckListCreator()
    ex.show()
    sys.exit(app.exec_())

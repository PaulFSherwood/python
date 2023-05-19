# import mainwindow.py and start the application
from mainwindow import MainWindow
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = MainWindow(app)
window.show()
app.exec()

from PySide6.QtWidgets import QApplication
from widget import Widget
import sys

app = QApplication(sys.argv)
Widget = Widget()
Widget.show()
app.exec()
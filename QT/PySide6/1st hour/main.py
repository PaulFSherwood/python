# VERSION3
import sys
from PySide6.QtWidgets import QApplication
from window_setup import WindowSetup

# Create an application object
app = QApplication(sys.argv)

# Create a window
window = WindowSetup()
# Display the window
window.setup()
window.show()

# Start the event loop
app.exec()
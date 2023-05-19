from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # Declare an app memeber
        self.setWindowTitle("Custom MainWindow")
        self.setWindowIcon(QIcon("icon.png"))
        self.setMinimumSize(QSize(480, 320))
        
        # Menu Bar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.app.quit)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # A bunch of other menu options just for the fun of it
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Help")

        # Working with toolbars
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # add the quit actio to the toolbar
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        # pass variable to lambda function so the called function knows which button was clicked
        action1.triggered.connect(lambda: self.toolbar_button_clicked("action1"))
        toolbar.addAction(action1)

        action2 = QAction(QIcon("icon.png"), "Another Action", self)
        action2.setStatusTip("Status message for another action")
        # Pass variable to a PyQt6 connected function using a lambda function
        action2.triggered.connect(lambda: self.toolbar_button_clicked("ICON"))
        #action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()  # seperate toolbar actions
        toolbar.addWidget(QPushButton("Click Here"))

        # Creat a status bar at the bottom
        self.setStatusBar(QStatusBar(self))

    def quit_app(self):
        self.app.quit()

    def toolbar_button_clicked(self, input):
        print("A toolbar button was clicked ", input)
        self.statusBar().showMessage("A toolbar button was clicked "+ input, 2000)

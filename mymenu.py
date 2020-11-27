import sys # to exit the program
                            # event loop  # look at  # window # buttons    # lay to put work
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp


class MenuDemo(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create menu bar
        bar = self.menuBar()

        # create root menus
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # create action for menu
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('Ctrl+Q')

        find_action = QAction('Find...', self)

        replace_action = QAction('Replace...', self)

        # add actions to menu
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(quit_action)

        find_menu = edit.addMenu('Find')
        find_menu.addAction(find_action)
        find_menu.addAction(replace_action)

        # test_menu = find_menu.addMenu('Test')
        # test_menu.addAction(quit_action)
        # test_menu.addAction(find_action)

        # events
        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.selected)

        self.setWindowTitle("MyMenus")
        self.resize(600, 400)

        self.show()

    def quit_trigger(self):
        qApp.quit()

    def selected(self, q):
        print(q.text() + ' selected')


app = QApplication(sys.argv)
writer = MenuDemo()
sys.exit(app.exec_())
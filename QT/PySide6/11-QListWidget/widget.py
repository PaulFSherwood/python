from PySide6.QtWidgets import (QWidget, QCheckBox, QHBoxLayout, QVBoxLayout,
                               QListWidget, QAbstractItemView, QPushButton)
from PySide6.QtGui import QFont


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget Demo")

        self.current_font = QFont()  # Current font
        self.current_font.setWeight(QFont.Bold)  # Use 'setWeight' instead of 'setWeight'
        self.regular_font = QFont()  # Regular font
        self.regular_font.setWeight(QFont.Normal)  # Use 'setWeight' instead of 'setWeight'

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem("One")
        self.list_widget.addItems(["Two", "Three"])
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)

        button_add_item = QPushButton("Add Item")
        button_add_item.clicked.connect(self.add_item)

        button_delete_item = QPushButton("Delete Item")
        button_delete_item.clicked.connect(self.delete_item)

        button_item_count = QPushButton("Item Count")
        button_item_count.clicked.connect(self.item_count)

        button_selected_items = QPushButton("Selected Items")
        button_selected_items.clicked.connect(self.selected_items)



        v_layout = QVBoxLayout()
        v_layout.addWidget(self.list_widget)
        v_layout.addWidget(button_add_item)
        v_layout.addWidget(button_delete_item)
        v_layout.addWidget(button_item_count)
        v_layout.addWidget(button_selected_items)

        self.setLayout(v_layout)

    def current_item_changed(self, current, previous):
        print("Current item changed from", previous.text())
        if previous is not None:
            previous.setFont(self.regular_font)

        if current is not None:
            current.setFont(self.current_font)
        
        # print(self.list_widget.selectedItems())
        # # Check if all items are unselected
        # if self.list_widget.selectedItems() == []:
        #     print("No items selected")
        #     # loop through list and set all items to regular font
        #     for index in range(self.list_widget.count()):
        #         item = self.list_widget.item(index)
        #         item.setFont(self.regular_font)

    def current_text_changed(self, text):
        print("Current text changed from", text)
        for index in range(self.list_widget.count()):  # Use 'self.list_widget.count()' instead of 'self.count()'
            item = self.list_widget.item(index)  # Use 'self.list_widget.item(index)' instead of 'self.item(index)'
            if item.text() == text:
                item.setFont(self.current_font)
            else:
                item.setFont(self.regular_font)

    def add_item(self):
        # Add item with the index number
        self.list_widget.addItem("New Item " + str(self.list_widget.count()))

    def delete_item(self):
        for item in self.list_widget.selectedItems():
            self.list_widget.takeItem(self.list_widget.row(item))

    def item_count(self):
        print("Item count:", self.list_widget.count())

    def selected_items(self):
        print("Selected items:")
        for item in self.list_widget.selectedItems():
            print(item.text())

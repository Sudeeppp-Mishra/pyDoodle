import sys
from PySide6.QtWidgets import QWidget, QApplication, QListWidget, QAbstractItemView, QVBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget")
        self.setFixedSize(400, 400)
        
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
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.list_widget)
        vbox.addWidget(button_add_item)
        vbox.addWidget(button_delete_item)
        vbox.addWidget(button_item_count)
        vbox.addWidget(button_selected_items)
        
    def current_item_changed(self, item):
        print("Current item: ", item.text())
    
    def current_text_changed(self, text):
        print("Current text changed: ", text)
        
    def add_item(self):
        pass
    
    def delete_item(self):
        pass
    
    def item_count(self):
        pass
    
    def selected_items(self):
        pass
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
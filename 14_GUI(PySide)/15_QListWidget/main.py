import sys
from PySide6.QtWidgets import QWidget, QApplication, QListWidget, QAbstractItemView, QVBoxLayout

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
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.list_widget)
        
    def current_item_changed(self, item):
        print("Current item: ", item.text())
    
    def current_text_changed(self, text):
        print("Current text changed: ", text)
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
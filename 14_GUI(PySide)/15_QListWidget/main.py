import sys
from PySide6.QtWidgets import QWidget, QApplication, QListWidget, QAbstractItemView, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget")
        
        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem("One")
        self.list_widget.addItems(["Two", "Three"])
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.list_widget)
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
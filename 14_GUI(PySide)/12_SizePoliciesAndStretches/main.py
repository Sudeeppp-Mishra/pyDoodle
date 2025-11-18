import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Size Policies and Stretches")
        
        
app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
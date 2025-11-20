import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Demo")
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
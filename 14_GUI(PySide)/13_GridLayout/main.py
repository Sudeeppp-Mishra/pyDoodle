import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Demo")
        
        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        button_4 = QPushButton("Four")
        button_5 = QPushButton("Five")
        button_6 = QPushButton("Six")
        button_7 = QPushButton("Seven")
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QLineEdit

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Size Policies and Stretches")
        
        # Size Policy: how the widgets behaves if container space is expanded or shrunk
        label = QLabel("Some Text: ")
        line_edit = QLineEdit()
        
        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)
        
        
app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
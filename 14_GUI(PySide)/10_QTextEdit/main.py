import sys
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit")
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
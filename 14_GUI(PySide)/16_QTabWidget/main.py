import sys
from PySide6.QtWidgets import QApplication, QWidget

class Widget(QWidget):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
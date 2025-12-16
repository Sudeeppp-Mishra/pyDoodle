from PySide6.QtWidgets import QWidget, QApplication
import sys

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox Demo")
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
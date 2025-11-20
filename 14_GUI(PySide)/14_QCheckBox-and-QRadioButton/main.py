from PySide6.QtWidgets import QApplication, QWidget
import sys

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox and QRadioButton")
        
        
app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
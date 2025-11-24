from PySide6.QtWidgets import QApplication, QWidget, QGroupBox, QCheckBox
import sys

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox and QRadioButton")
        
        os = QGroupBox("Choose Operating Systems")
        
        
app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
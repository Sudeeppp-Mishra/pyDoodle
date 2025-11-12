import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel and QLineEdit")
        
        # A set of signal we can connect to 
        label = QLabel("Fullname: ")
        self.line_edit = QLineEdit()
        button = QPushButton("Grab Data")
        self.text_holder_label = QLabel("I AM HERE")
        
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(self.line_edit)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(button)
        vbox.addWidget(self.text_holder_label)
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
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
        
        button.clicked.connect(self.button_clicked)
        self.line_edit.textChanged.connect(self.text_changed)
        
        self.setLayout(vbox)
        
    # Slots
    def button_clicked(self):
        self.text_holder_label.setText(self.line_edit.text())
        
    def text_changed(self):
        print("Text changed to ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
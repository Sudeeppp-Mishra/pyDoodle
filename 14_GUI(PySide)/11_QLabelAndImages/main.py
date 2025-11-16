import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLable and Images")
        
        image_label = QLabel()
        image_label.setPixmap(QPixmap("images/nature.jpg"))
        
        vbox = QVBoxLayout()
        vbox.addWidget(image_label)
        
        self.setLayout(vbox)
    
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
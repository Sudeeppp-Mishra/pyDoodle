import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLable and Images")
        
        image_label = QLabel()
        
        pixmap = QPixmap("images/nature.jpg")
        
        scaled_pixmap = pixmap.scaled(400, 300)
        
        image_label.setPixmap(scaled_pixmap)
        
        vbox = QVBoxLayout()
        vbox.addWidget(image_label)
        
        self.setLayout(vbox)
    
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
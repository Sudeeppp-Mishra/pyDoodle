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
        
        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        
        # stretch: how much of the available space (in the layout) is occupied by each widget.
        # you specify the stretch when you add things to the layout : button_1 takes up 2 units, button_2 and button_3 take up 1 unit
        
        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1, 2)
        h_layout_2.addWidget(button_2, 1)
        h_layout_2.addWidget(button_3, 1)
        
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)
        
        self.setLayout(v_layout)
        
app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
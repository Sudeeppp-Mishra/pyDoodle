from PySide6.QtWidgets import QWidget, QApplication, QComboBox, QPushButton, QVBoxLayout
import sys

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox Demo")
        
        self.combo_box = QComboBox(self);
        # Add planets to the combobox
        self.combo_box.addItem("Earth")
        self.combo_box.addItem("Venus")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Jupiter")
        self.combo_box.addItem("Saturn")
        
        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        button_set_current = QPushButton("Set value")
        button_set_current.clicked.connect(self.set_current)
        button_get_values = QPushButton("Get values")
        button_get_values.clicked.connect(self.get_values)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.combo_box)
        vbox.addWidget(button_current_value)
        vbox.addWidget(button_set_current)
        vbox.addWidget(button_get_values)
        
        self.setLayout(vbox)
        
    def current_value(self):
        print("Current item: ", self.combo_box.currentText(), " - current index: ", self.combo_box.currentIndex())
    
    def set_current(self):
        pass
    
    def get_values(self):
        pass
    
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
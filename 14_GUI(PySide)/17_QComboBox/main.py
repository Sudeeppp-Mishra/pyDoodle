from PySide6.QtWidgets import QWidget, QApplication, QComboBox, QPushButton
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
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
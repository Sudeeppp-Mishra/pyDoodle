from PySide6.QtWidgets import QWidget, QApplication, QComboBox
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
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
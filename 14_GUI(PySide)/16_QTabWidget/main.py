import sys
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QLineEdit, QLabel, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget Demo")
        
        tab_widget = QTabWidget(self)
        
        # Information
        widget_form = QWidget()
        label_full_name = QLabel("Full name: ")
        line_edit_full_name = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(form_layout)

app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
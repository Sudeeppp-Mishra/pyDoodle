from PySide6.QtWidgets import QApplication, QWidget, QGroupBox, QCheckBox, QVBoxLayout
import sys

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox and QRadioButton")
        
        os = QGroupBox("Choose Operating Systems")
        windows = QCheckBox("Windows")
        
        linux = QCheckBox("Linux")
        
        mac = QCheckBox("Mac")
        
        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(os)
        self.setLayout(main_layout)
        
app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
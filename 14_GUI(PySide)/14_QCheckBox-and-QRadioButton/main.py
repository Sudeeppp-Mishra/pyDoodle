from PySide6.QtWidgets import QApplication, QWidget, QGroupBox, QCheckBox, QVBoxLayout, QButtonGroup, QRadioButton
import sys

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox and QRadioButton")
        
        os = QGroupBox("Choose Operating Systems")
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)
        
        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)
        
        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)
        
        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)
        
        drinks = QGroupBox("Choose your drink")
        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)
        
        # Make the checkboxes exclusive
        exclusive_button_group = QButtonGroup(self) # The self parent is needed here
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.setExclusive(True)
        
        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(coffee)
        drink_layout.addWidget(juice)
        drinks.setLayout(drink_layout)
        
        # Radio Buttons: answers
        answers = QGroupBox("Choose Answer")
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_a.setChecked(True)
    
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(os)
        main_layout.addWidget(drinks)
        self.setLayout(main_layout)
        
    def windows_box_toggled(self, checked):
        if checked:
            print("Windows box checked")
        else:
            print("Windows box unchecked")
    
    def linux_box_toggled(self, checked):
        if checked:
            print("Linux box checked")
        else:
            print("Linux box unchecked")
            
    def mac_box_toggled(self, checked):
        if checked:
            print("Mac box checked")
        else:
            print("Mac box unchecked")
            
app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
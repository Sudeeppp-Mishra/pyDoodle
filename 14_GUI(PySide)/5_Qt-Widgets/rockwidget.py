from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")
        
        button1 = QPushButton("BUTTON 1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("BUTTON 2")
        button2.clicked.connect(self.button2_clicked)
        
        vbox = QVBoxLayout()
        
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        
        self.setLayout(vbox)
        
    def button1_clicked(self):
        print("Button 1 Clicked!")
        
    def button2_clicked(self):
        print("Button 2 Clicked!")
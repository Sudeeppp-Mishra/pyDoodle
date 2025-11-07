# also taking the parameter clicked([checked=false])

import sys
from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked(data):
    print("You clicked the button, didn't you! Checked: ", data)
    
app = QApplication()
button = QPushButton("Press ME")
button.setCheckable(True) # Makes the button checkable. It's unchecked by default.
                          # Further clicks toggle between checked and unchecked states
                          
button.clicked.connect(button_clicked)

button.show()
sys.exit(app.exec())
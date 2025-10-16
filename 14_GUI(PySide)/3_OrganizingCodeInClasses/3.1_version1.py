# VERSION1 : Setting everything up in the global scope
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App!")
# Think of QMainWindow as:
# 	•	The main application window (like in big apps: Word, VS Code, etc.)
# 	•	Comes with built-in structure:
# 	    •	Menu bar (File, Edit, etc.)
# 	    •	Toolbars
# 	    •	Status bar
# 	    •	Central widget area

# Basically, QMainWindow gives you a ready-made framework for complex applications.


button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()
app.exec()
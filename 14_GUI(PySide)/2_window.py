#Importing the components we need
from PySide6.QtWidgets import QApplication, QWidget

#The sys module is responsible for processing command line arguments
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

# Think of QWidget as:
# 	•	The simplest window/container in Qt.
# 	•	A blank rectangle where you can place other widgets (buttons, labels, etc.).
# 	•	Doesn’t come with any built-in menus, toolbars, or status bars.

# When to use QWidget:
# 	•	You just need a simple custom window.
# 	•	You’re building a small dialog, popup, or tool window.
# 	•	You want full control over layout and appearance.

#Start the event loop
app.exec()
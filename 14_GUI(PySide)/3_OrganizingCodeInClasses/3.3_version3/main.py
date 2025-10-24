from buttonHolderClass import ButtonHolder
import sys
from PySide6.QtWidgets import QApplication
 
app = QApplication(sys.argv)
 
window = ButtonHolder()
window.show()
app.exec()
from PySide6.QtWidgets import QApplication, QWidget
import sys
from rockwidget import RockWidget

app = QApplication(sys.argv)

window = RockWidget()
window.show()

sys.exit(app.exec())
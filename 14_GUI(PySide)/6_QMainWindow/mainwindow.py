from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom MainWindow")
        
        # Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        
        new_action = QAction("╳", self)
        file_menu.addAction(new_action)
        new_action.triggered.connect(self.close)
        
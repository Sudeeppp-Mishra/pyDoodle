from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom MainWindow")
        
        # Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        # Notes on Menu Bar and '&' in PySide6 / PyQt

        # - In PySide6/PyQt, menu bars are created using `QMenuBar` and menu items with `QMenu` and `QAction`.
        # - The `&` symbol in menu or action names is used to **define a keyboard shortcut (mnemonic)**.
        
        # Example:

        # ```python
        # file_menu = menu_bar.addMenu("&File")  # 'F' becomes the mnemonic; Alt + F to open it; but in mac it's not visible visually
        # new_action = QAction("&New", self)     # 'N' becomes the mnemonic
        
        quit_action = QAction("╳", self)
        file_menu.addAction(quit_action)
        quit_action.triggered.connect(self.close)
        
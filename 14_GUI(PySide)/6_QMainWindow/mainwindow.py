from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize

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
        
        edit_menu = menu_bar.addMenu("Edit")
        
        copy_action = QAction("Copy", self)
        edit_menu.addAction(copy_action)
        cut_action = QAction("Cut", self)
        edit_menu.addAction(cut_action)
        paste_action = QAction("Paste", self)
        edit_menu.addAction(paste_action)
        undo_action = QAction("Undo", self)
        edit_menu.addAction(undo_action)
        redo_action = QAction("Redo", self)
        edit_menu.addAction(redo_action)
        
        window_menu = menu_bar.addMenu("Window")
        settings_menu = menu_bar.addMenu("Setting")
        help_menu = menu_bar.addMenu("Help")
        
                # ----- Dummy actions -----
        # These do nothing, but they force macOS to show the menu.

        dummy_win = QAction(" ", self)      # blank action
        dummy_win.setEnabled(False)         # make it unclickable
        window_menu.addAction(dummy_win)

        dummy_set = QAction(" ", self)
        dummy_set.setEnabled(False)
        settings_menu.addAction(dummy_set)

        dummy_help = QAction(" ", self)
        dummy_help.setEnabled(False)
        help_menu.addAction(dummy_help)
        
        
        # WORKING WITH TOOLBARS
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(toolbar)
        
        # Add the quit action to the toolbar
        toolbar.addAction(quit_action)
        
        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)
        
    def toolbar_button_click(self):
        print("action 1 triggered")
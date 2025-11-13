import sys
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit")
        
        self.text_edit = QTextEdit()
        
        # Buttons
        copy_button = QPushButton("Copy")
        
        cut_button = QPushButton("Cut")
        
        paste_button = QPushButton("Paste")
        
        undo_button = QPushButton("Undo")
        
        redo_button = QPushButton("Redo")
        
        set_plain_text_button = QPushButton("Set Plain Text")
        
        set_html_button = QPushButton("Set HTML")
        
        clear_button = QPushButton("Clear")
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
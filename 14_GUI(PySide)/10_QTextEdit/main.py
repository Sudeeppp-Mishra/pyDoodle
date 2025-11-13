import sys
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit")
        
        self.text_edit = QTextEdit()
        
        # Buttons
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy)
        
        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)
        
        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste)
        
        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)
        
        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)
        
        set_plain_text_button = QPushButton("Set Plain Text")
        set_plain_text_button.clicked.connect(self.text_edit.set_plain_text)
        
        set_html_button = QPushButton("Set HTML")
        set_html_button.clicked.connect(self.text_edit.set_html)
        
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
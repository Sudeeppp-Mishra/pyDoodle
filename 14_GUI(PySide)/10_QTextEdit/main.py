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
        set_plain_text_button.clicked.connect(self.set_plain_text)
        
        set_html_button = QPushButton("Set HTML")
        set_html_button.clicked.connect(self.set_html)
        
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)
        
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        
        hbox.addWidget(copy_button)
        hbox.addWidget(cut_button)
        hbox.addWidget(paste_button)
        hbox.addWidget(undo_button)
        hbox.addWidget(redo_button)
        hbox.addWidget(set_plain_text_button)
        hbox.addWidget(set_html_button)
        hbox.addWidget(clear_button)
        
        vbox.addLayout(hbox)
        vbox.addWidget(self.text_edit)
        
        self.setLayout(vbox)
        
    def set_plain_text(self):
        pass
    
    def set_html(self):
        pass
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
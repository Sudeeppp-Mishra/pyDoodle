import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel and QLineEdit")
        
        # A set of signal we can connect to 
        label = QLabel("Fullname: ")
        self.line_edit = QLineEdit()
        button = QPushButton("Grab Data")
        self.text_holder_label = QLabel("I AM HERE")
        
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(self.line_edit)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(button)
        vbox.addWidget(self.text_holder_label)
        
        button.clicked.connect(self.button_clicked)
        #self.line_edit.textChanged.connect(self.text_changed)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        # self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)
        
        self.setLayout(vbox)
        
    # Slots
    def button_clicked(self):
        self.text_holder_label.setText(self.line_edit.text())
        
    def text_changed(self):
        print("Text changed to ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())
        
    def cursor_position_changed(self, old_position, new_position):
        print("cursor old position: ", old_position, " -new position: ", new_position)
        
    def editing_finished(self): # this triggers after we type enter/return then the signal gets connected to the slot
        print("Editing finished!")
        
    def return_pressed(self): # it's kinda same as editing finished and it gets triggered after user presses enter
        print("Return pressed!")
        
    def selection_changed(self):
        print("Selection changed: ", self.line_edit.selectedText()) # this returns the text we select in line edit field
        
    def text_edited(self, edited_new_text):
        print("Text edited. New tex: ", edited_new_text)
        
app = QApplication(sys.argv)
widget = Widget()

widget.show()
sys.exit(app.exec())
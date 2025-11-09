import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.hard_way_button = QPushButton("Hard Way", self)
        self.hard_way_button.clicked.connect(self.button_clicked_hard)
        
        self.button_critical = QPushButton("Critical")
        self.button_critical.clicked.connect(self.button_clicked_critical)
        
        self.button_question = QPushButton("Question")
        self.button_question.clicked.connect(self.button_clicked_question)
        
        self.button_information = QPushButton("Information")
        self.button_information.clicked.connect(self.button_clicked_information)
        
        self.button_warning = QPushButton("Warning")
        self.button_warning.clicked.connect(self.button_clicked_warning)
        
        self.button_about = QPushButton("About")
        self.button_about.clicked.connect(self.button_clicked_about)
        
        self.central_widget = QWidget()
        self.vbox = QVBoxLayout()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QMessageBox")
        
        self.vbox.addWidget(self.hard_way_button)
        self.vbox.addWidget(self.button_critical)
        self.vbox.addWidget(self.button_question)
        self.vbox.addWidget(self.button_information)
        self.vbox.addWidget(self.button_warning)
        self.vbox.addWidget(self.button_about)
        
        self.central_widget.setLayout(self.vbox)
        self.setCentralWidget(self.central_widget)
        
    def button_clicked_hard(self):
        pass
    
    def button_clicked_critical(self):
        pass
    
    def button_clicked_question(self):
        pass
    
    def button_clicked_information(self):
        pass
    
    def button_clicked_warning(self):
        pass
    
    def button_clicked_about(self):
        pass
        

if __name__=="__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()
    sys.exit(app.exec())
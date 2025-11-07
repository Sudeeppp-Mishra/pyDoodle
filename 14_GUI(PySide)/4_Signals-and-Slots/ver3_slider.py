from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QApplication, QSlider
import sys

# The slot: responds when sth happens
def respond_to_slider(data):
    print("Slider moved to: ", data)
    
app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# You just do teh connection. The Qt system takes care of passing the data from the signal to the slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()
sys.exit(app.exec())
# VERSION1: Just responding to the button click: syntax
from PySide6.QtWidgets import QApplication, QPushButton
import sys

app = QApplication(sys.argv)

button = QPushButton("Click Me!")

# The slot: responds when something happens
def button_clicked():
    print("You clicked the button, didn't u??")
   
# clicked is a signal of QPushButton. It's emitted when you click on the button
# You can wire a slot to the signal using the syntax below: 
button.clicked.connect(button_clicked)
    
button.show()
sys.exit(app.exec())
# 🧠 PySide6 / PyQt — Understanding app.exec(), app.exec_(), and sys.exit(app.exec())

# When you create a Qt application:
# app = QApplication(sys.argv)

# The GUI won’t actually "run" until you start the event loop.
# The event loop is what keeps your window alive and responsive —
# it listens for clicks, key presses, redraws, and all real-time UI updates.

# ▶️ To start the event loop:
# app.exec()      → used in PySide6 and PyQt6
# app.exec_()     → used in older versions (PySide2 and PyQt5)

# 🔍 Why two different names?
# In Python, "exec" used to be a reserved keyword in older versions (Python 2),
# so Qt developers added an underscore (exec_()) to avoid conflicts.
# In modern Python (3.x), "exec" is safe to use again, so new Qt bindings
# (PySide6 / PyQt6) dropped the underscore and just use app.exec().

# ✅ So:
# PyQt5 / PySide2 → app.exec_()
# PyQt6 / PySide6 → app.exec()

# 🔄 What it does:
# - Starts the Qt event loop (the "main loop" of your app)
# - Keeps your app running until the user closes it
# - When closed, returns an exit code:
#     0  → normal exit
#     1+ → error or abnormal termination

# So technically, this is valid:
# app.exec()

# But the best practice is:
# sys.exit(app.exec())

# 🧩 Why wrap in sys.exit()?
# sys.exit() ensures Python terminates cleanly using the same exit code
# returned by the Qt application. 
# This is important when:
#   - You run the app from another script or process
#   - You want the OS/shell to know if your app ended normally

# 💡 In short:
# app.exec() or app.exec_()   → starts the event loop (fine for small tests)
# sys.exit(app.exec())        → starts the loop + exits cleanly (best practice)

# ✅ Always use sys.exit(app.exec()) in real projects (PySide6 / PyQt6).
# ✅ For older codebases (PyQt5 / PySide2), use sys.exit(app.exec_()) instead.



##########################################################################################

# PySide6 — Understanding QMainWindow vs showing a widget directly

# Any QWidget (like QPushButton, QLabel, etc.) can be shown directly.
# When you call .show() on it, PySide treats it as a standalone top-level window.
# Example:
# button = QPushButton("Click Me!")
# button.show()
# → The button itself becomes its own window (simple for quick tests or demos).

# 🏛️ QMainWindow is used when you want a full application window.
# It provides structure for:
#   - Menus
#   - Toolbars
#   - Status bar
#   - Central widget (main area where you place layouts & controls)
# Example:
# window = QMainWindow()
# button = QPushButton("Click Me!", window)
# window.show()
# → The button is placed *inside* the main window.

# 💡 In short:
# Use .show() directly → for simple, one-widget apps or quick UI tests.
# Use QMainWindow (or QWidget subclass) → for real multi-widget applications.

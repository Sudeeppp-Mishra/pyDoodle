# 🧠 PySide6 / PyQt — QMainWindow Notes

---

## 1. What is QMainWindow?

- `QMainWindow` is a **specialized QWidget** designed to be the main window of a desktop application.  
- It provides a **predefined structure** to organize the main GUI elements efficiently.

---

## 2. Key Features

- **Menu Bar (`QMenuBar`)**:  
  - Standard location at the top of the window for menus like File, Edit, Help.
- **Toolbars (`QToolBar`)**:  
  - Horizontal or vertical bars for shortcut actions, usually under the menu bar.
- **Status Bar (`QStatusBar`)**:  
  - A bar at the bottom to display messages, hints, or app status.
- **Central Widget**:  
  - The main area where you place your primary content (layouts, widgets, forms).
  - Can only have **one central widget**; other widgets must be added inside it via layouts.

---

## 3. Why use QMainWindow?

- Provides **standard desktop application structure** out of the box.  
- Simplifies organizing menus, toolbars, status bar, and central content.  
- Ensures consistent look-and-feel with native OS standards.  
- Supports **parent-child widget hierarchy** like all QWidget-derived classes.

---

## 4. Parent-Child Concept

- `QMainWindow` itself is a **QWidget**.  
- Child widgets can be added as **central widget**, toolbars, menus, or dock widgets.  


---

## 5. Key Concepts / Best Practices

- Always set a **central widget** using `setCentralWidget()`.  
- Use **layouts** inside the central widget instead of fixed geometry.  
- Menus and toolbars are optional but recommended for structured applications.  
- Signals and slots work as usual to connect actions (e.g., menu clicks, button clicks).

---

### 💡 TL;DR

- `QMainWindow` = specialized QWidget for main app window.  
- Provides **MenuBar, ToolBar, StatusBar, CentralWidget**.  
- Use it when building real desktop applications with multiple widgets.  
- Always use layouts and central widget to organize content.

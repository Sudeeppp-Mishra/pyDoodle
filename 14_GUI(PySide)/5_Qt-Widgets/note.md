# QWidget

Fundamental UI component in Qt

# PySide6 / PyQt — QWidget and QtWidgets Notes (Theoretical)

---

## 1. QtWidgets Module

- `QtWidgets` is the **module that contains all user interface widgets** in PyQt/PySide.
- It includes:
  - **Base widgets**: `QWidget`, `QMainWindow`, `QDialog`
  - **Input widgets**: `QLineEdit`, `QSpinBox`, `QCheckBox`
  - **Buttons**: `QPushButton`, `QRadioButton`
  - **Layouts/Containers**: `QVBoxLayout`, `QHBoxLayout`, `QGridLayout`
  - **Menus & Toolbars**: `QMenuBar`, `QToolBar`
  - **Other elements**: `QLabel`, `QTabWidget`, `QListWidget`

---

## 2. QWidget

- `QWidget` is the **base class for all visible UI elements** in Qt.
- All GUI widgets inherit from `QWidget`.
- **Parent-child relationship**:
  - Child widgets are drawn inside their parent.
  - Child widgets are destroyed automatically when the parent is destroyed.
- **Standalone QWidget** can act as its own window if no parent is provided.
- Layouts are applied to `QWidget` to manage child widgets automatically.

---

## 3. Common QWidget Types

| Widget | Description |
|--------|-------------|
| `QWidget` | Base class for all visible widgets; can be a window or container |
| `QMainWindow` | Main application window; supports menu bar, toolbars, status bar, and central widget |
| `QDialog` | Popup or modal window for forms/messages |
| `QLabel` | Displays text or images; non-interactive |
| `QPushButton` | Clickable button |
| `QLineEdit` | Single-line text input |
| `QRadioButton` / `QCheckBox` | Selection controls used in forms |
| `QTabWidget` | Container with multiple tab pages |
| `QFrame` | Visual container; can have borders or grouping |

---

## 4. QWidget Hierarchy (Conceptual)

- `QWidget` is the **base class** for all other widgets.
- `QMainWindow` and `QDialog` are specialized QWidget types.
- Other widgets like buttons, labels, checkboxes, and layouts inherit from QWidget.
- Parent widgets contain child widgets forming a hierarchy:
  - `QMainWindow` → Menu bar, Status bar, Central widget
  - `QWidget` → Buttons, Labels, Inputs
  - `QDialog` → Popup windows

---

## 5. Key Concepts

- **Parent-Child**: Determines placement and lifetime of widgets.
- **Visibility**: Widgets are displayed only after `.show()`.
- **Layouts**: Organize child widgets; preferable to fixed geometry.
- **Signals and Slots**: Mechanism for widget communication and event handling.

---

### 💡 Summary

- `QtWidgets` → module containing all GUI widgets.  
- `QWidget` → base class for all visible widgets.  
- Specialized widgets (`QMainWindow`, `QDialog`, etc.) inherit from `QWidget`.  
- Parent-child hierarchy and layouts are core to managing GUI structure.  
- Signals and slots enable interactive communication between widgets.

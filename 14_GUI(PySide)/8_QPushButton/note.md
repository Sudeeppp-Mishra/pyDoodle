# QPushButton — Notes

`QPushButton` is a clickable button widget in Qt used to trigger actions, submit forms, and control application behavior.

---

## Key Concepts

### • Creating a Button
A button can be created using only text, only an icon, or both.  
It can optionally have a parent widget.

### • Styling
Buttons can be customized using:
- `setStyleSheet()` (CSS-like Qt styles)
- Custom fonts
- Object names for targeted styling
- Icons

### • States
`QPushButton` supports:
- Normal  
- Hover  
- Pressed  
- Disabled  
- Checked (if toggleable)

---

## QPushButton Signals (Complete List)

### **1. `clicked(bool checked=False)`**
Emitted when the button is clicked.

### **2. `pressed()`**
Emitted when the user presses (but has not yet released) the button.

### **3. `released()`**
Emitted when the user releases the button.

### **4. `toggled(bool checked)`**
Emitted when the button’s checkable state changes.  
Only applies if `setCheckable(True)` is enabled.

---

## Checkable Buttons
Enabling toggle behavior:

- `setCheckable(True)`  
The button will maintain an ON/OFF state.
Useful for switches, modes, or options.

---

## Common Uses
- Submitting forms  
- Triggering actions  
- Opening dialogs  
- Changing views  
- Starting/stopping processes  
- Acting as an ON/OFF toggle (with `toggled`)

---

## Summary
`QPushButton` is one of the most essential interactive widgets in Qt.  
It provides several signals (`clicked`, `pressed`, `released`, and `toggled`), supports custom styling, icons, and toggle states, and forms the backbone of most user interactions in PyQt/PySide applications.
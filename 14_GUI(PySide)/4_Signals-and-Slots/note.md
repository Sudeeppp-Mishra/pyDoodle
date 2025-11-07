# Signals and Slots — PyQt / PySide6 (Theory Notes)

Signals and Slots form the backbone of event-driven programming in Qt. They are used for communication between objects, especially in GUI applications.

---

## What Are Signals?

- A **signal** is an event notification.
- It is emitted when something happens inside a widget or object (e.g., a button is clicked, text changes, a timer finishes).
- Signals carry information that “something occurred.”
- Most widgets have **built-in signals**, and you can also define custom ones.

---

## What Are Slots?

- A **slot** is a function that gets executed when a connected signal is emitted.
- Slots can be:
  - Normal Python functions  
  - Methods inside classes  
  - Built-in Qt slots  
- A signal can be connected to multiple slots, and multiple signals can connect to the same slot.

---

## Connecting Signals to Slots

- Signals and slots are connected using `.connect()`.
- After connection, when the signal fires, the slot runs automatically.
- This allows clean communication without continuous polling or manual checks.

---

## Why Signals & Slots Are Important

- They allow **automatic reaction** to user actions and system events.
- They keep code modular and decoupled.
- They enable clean communication between UI components.
- They are essential for:
  - GUI interactions  
  - Background tasks  
  - Threading (safe UI updates)

---

## Custom Signals (Concept)

- You can define your own signals if default ones are not enough.
- Custom signals can also carry data types (e.g., int, str).
- Custom signals help create more structured and extendable applications.

---

## Signals That Carry Data

- Some built-in signals emit extra information (e.g., new text, slider value, index).
- Slots must accept the correct parameters matching the signal.

---

## Threading & Signals (Concept)

- Signals/slots allow threads to safely communicate with the main GUI thread.
- A worker thread can emit a signal, and the UI reacts without freezing.

---

## Summary (Quick Points)

- **Signal:** Announces an event.
- **Slot:** Handles the event.
- **connect():** Links signal → slot.
- Signals help achieve clean, event-driven architecture.
- Widely used in all GUI elements and threading in PyQt/PySide6.
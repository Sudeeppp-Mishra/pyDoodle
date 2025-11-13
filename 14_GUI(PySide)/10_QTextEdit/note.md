# QTextEdit — PySide6 / PyQt5

## Overview
`QTextEdit` is a **multi-line text editing widget** in PySide6/PyQt5.  
It allows users to **display, edit, and format rich text (HTML or plain text)**.  
It’s commonly used for notes, document editors, or input fields requiring multiple lines.

---

## Key Features
- Supports **plain text** and **rich text (HTML)**.
- Provides **undo/redo**, **cut/copy/paste**, and **drag-and-drop** functionality.
- Supports **text alignment, font, color, and style customization**.
- Scrollbars automatically appear when text overflows.
- Can be set **read-only** for display-only purposes.

---

## Common Methods

| Method | Description |
|--------|--------------|
| `setText(str)` | Sets the text (clears existing content). |
| `toPlainText()` | Returns the text as plain string. |
| `setHtml(str)` | Sets the text with HTML formatting. |
| `toHtml()` | Returns the text as HTML. |
| `append(str)` | Appends text to the end (adds a newline automatically). |
| `insertPlainText(str)` | Inserts plain text at the cursor position. |
| `clear()` | Clears all text. |
| `setReadOnly(bool)` | Makes the editor read-only (non-editable). |
| `setPlaceholderText(str)` | Displays placeholder text when empty. |
| `setFont(QFont)` | Sets the font for the text. |
| `setAlignment(Qt.Alignment)` | Aligns text (e.g., left, center, right). |
| `setTextColor(QColor)` | Changes text color. |

---

## Common Signals

| Signal | Description |
|--------|--------------|
| `textChanged()` | Emitted whenever the text content changes. |
| `cursorPositionChanged()` | Emitted when the cursor moves. |
| `selectionChanged()` | Emitted when text selection changes. |
| `copyAvailable(bool)` | Emitted when text is selected and can be copied. |
| `redoAvailable(bool)` | Emitted when redo operation becomes available/unavailable. |
| `undoAvailable(bool)` | Emitted when undo operation becomes available/unavailable. |

# QLabel and QLineEdit in PySide6

## QLabel

### Overview
`QLabel` is a widget used to display text or images in a PySide6 application. It is commonly used for static text, titles, instructions, or status information. Labels can also display images, HTML-formatted text, and can be made interactive (e.g., clickable links).

### Key Features
- Displays plain text, rich text (HTML), or images.
- Supports alignment (left, right, center, justify).
- Can detect and display hyperlinks.
- Can be used as a buddy for input widgets (using `setBuddy()`).

### Common Methods
| Method | Description |
|--------|--------------|
| `setText(text: str)` | Sets the text displayed by the label. |
| `text()` | Returns the label's text. |
| `setPixmap(pixmap: QPixmap)` | Displays an image instead of text. |
| `setAlignment(Qt.Alignment)` | Aligns the content (e.g., `Qt.AlignCenter`). |
| `setWordWrap(bool)` | Enables or disables word wrapping. |
| `setTextFormat(Qt.TextFormat)` | Sets the text format (plain, rich, auto). |
| `setBuddy(QWidget)` | Associates the label with an input widget. |
| `setStyleSheet(str)` | Applies CSS-like styling. |

### Signals
`QLabel` does not emit many signals by default, but when using rich text links:
- `linkActivated(str)` — emitted when a link is clicked.
- `linkHovered(str)` — emitted when hovering over a link.

---

## QLineEdit

### Overview
`QLineEdit` is a single-line text input widget. It allows users to enter and edit text and is commonly used for input fields such as names, emails, or search bars.

### Key Features
- Supports text alignment, masking, input validation, and auto-completion.
- Can hide input characters (e.g., for passwords).
- Can display placeholder text.
- Supports undo/redo and text selection.

### Common Methods
| Method | Description |
|--------|--------------|
| `setText(text: str)` | Sets the text in the input field. |
| `text()` | Returns the current text. |
| `setPlaceholderText(str)` | Displays gray hint text when empty. |
| `setEchoMode(QLineEdit.EchoMode)` | Controls text visibility (Normal, NoEcho, Password, PasswordEchoOnEdit). |
| `setAlignment(Qt.Alignment)` | Aligns the text horizontally or vertically. |
| `setReadOnly(bool)` | Makes the field read-only if `True`. |
| `setValidator(QValidator)` | Restricts input based on validation rules. |
| `setMaxLength(int)` | Limits the number of input characters. |
| `clear()` | Clears the text in the input field. |

### Common Signals
| Signal | Description |
|---------|--------------|
| `textChanged(str)` | Emitted whenever the text changes (even programmatically). |
| `textEdited(str)` | Emitted when the user manually edits the text. |
| `returnPressed()` | Emitted when the user presses *Enter/Return*. |
| `editingFinished()` | Emitted when editing is done (focus leaves the field). |
| `cursorPositionChanged(int, int)` | Emitted when the cursor moves. |
| `selectionChanged()` | Emitted when the text selection changes. |

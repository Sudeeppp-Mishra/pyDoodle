# QMessageBox (PySide6 / PyQt6)

`QMessageBox` is a built-in dialog class used to display messages to the user. It allows interaction through standard buttons and provides different types of message icons to convey meaning.

---

## Key Points

- **Purpose:** Display information, warnings, critical messages, or questions.
- **Dialog Types / Icons:**
  - `Information` – for general information.
  - `Warning` – for cautionary messages.
  - `Critical` – for errors or critical issues.
  - `Question` – for asking the user a decision.
- **Standard Buttons:**
  - `Ok`, `Cancel`, `Yes`, `No`, `Retry`, `Close`
  - Multiple buttons can be combined.
- **Modal Behavior:** The dialog blocks interaction with the parent window until closed.
- **Customizable Elements:**
  - Window title
  - Main text
  - Informative text
  - Detailed text (optional)
  - Icon type
  - Buttons

---

## Notes

- Typically used for user notifications, confirmations, or warnings.
- Supports additional details in a collapsible section.
- Provides a simple way to handle user responses through standard buttons.
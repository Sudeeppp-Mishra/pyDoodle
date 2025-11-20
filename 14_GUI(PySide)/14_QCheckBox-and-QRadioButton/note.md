# QCheckBox & QRadioButton — Theoretical Notes

## Overview
QCheckBox and QRadioButton are interactive input widgets in Qt used for selecting options.  
They provide boolean or mutually exclusive choices within a graphical user interface.

---

# QCheckBox — Theoretical Notes

## Purpose
- Represents an option that can be **checked** or **unchecked**.
- Supports a third **partially checked** (tri-state) state.
- Used when **multiple selections** are allowed.

## Key Features
- **States**:
  - Unchecked
  - Checked
  - Partially Checked (tri-state mode)
- **Text Label**: Attached descriptive text beside the checkbox.
- **User Interaction**: Clicking toggles between states.
- **Keyboard Interaction**: Spacebar toggles state when focused.
- **Focus Handling**: Visual indication when focused.
- **Check State Management**: Fully controllable programmatically.
- **Auto-Exclusive Behavior**: Not applicable (each checkbox independent).

## Use Cases
- Preferences and settings
- Enabling/disabling features
- Selecting multiple independent options

## Signals (Conceptual Only)
- State change notifications
- Toggled signal for boolean change
- Press and release interaction events

## Behavior Within Layouts
- Automatically adapts to resizing, layout rules, and style.
- Label text participates in size calculations.
- Consistent look across platforms due to Qt’s style system.

---

# QRadioButton — Theoretical Notes

## Purpose
- Represents a **single-choice option** within a group.
- Only **one** radio button in the same group can be active at a time.

## Key Features
- **Mutual Exclusivity**:
  - Radio buttons in the same parent or same QButtonGroup allow only one selection.
- **Text Label**: Descriptive text placed adjacent to the indicator.
- **User Interaction**:
  - Selecting one radio button deselects the others in the group.
- **Keyboard Navigation**:
  - Arrow keys for group navigation.
- **Programmatic Control**:
  - Can set or clear checked state, though clearing manually may be restricted depending on exclusivity.

## Use Cases
- Selecting one option among many
- Choosing modes, types, categories, or configurations
- Form inputs requiring exclusive choice

## Signals (Conceptual Only)
- Toggled signal when selection state changes
- Press/release interaction events

## Behavior Within Layouts
- Aligns neatly within forms and menu-like structures.
- Size depends on label text and style metrics.
- Works seamlessly in grids, vertical/horizontal layouts, and grouped interfaces.

---

# Differences Between QCheckBox and QRadioButton (Conceptual)
- QCheckBox: Multiple selectable options, independent.
- QRadioButton: Single selection within a group.
- QCheckBox: Can be tri-state.
- QRadioButton: Always binary (checked/unchecked) but exclusive in groups.
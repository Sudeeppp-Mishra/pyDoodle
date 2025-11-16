# PySide6 Size Policies and Stretches - Complete Guide

## Table of Contents
1. [Introduction](#introduction)
2. [QSizePolicy Overview](#qsizepolicy-overview)
3. [Policy Types](#policy-types)
4. [Size Policy Properties](#size-policy-properties)
5. [Stretch Factors](#stretch-factors)
6. [Practical Examples](#practical-examples)
7. [Best Practices](#best-practices)
8. [Common Patterns](#common-patterns)

---

## Introduction

Size policies and stretches in PySide6 control how widgets resize and distribute space within layouts. Understanding these concepts is crucial for creating responsive and professional GUI applications.

**Key Concepts:**
- **Size Policy**: Defines how a widget can grow or shrink
- **Stretch Factor**: Determines the proportion of space a widget receives
- **Size Hints**: Suggested sizes provided by widgets

---

## QSizePolicy Overview

### Basic Structure

```python
from PySide6.QtWidgets import QSizePolicy

# Create a size policy
policy = QSizePolicy(horizontal_policy, vertical_policy)

# Apply to widget
widget.setSizePolicy(policy)

# Or shorthand
widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
```

### Components of QSizePolicy

A size policy consists of:
1. **Horizontal Policy** - Controls width behavior
2. **Vertical Policy** - Controls height behavior
3. **Horizontal Stretch** - Priority for horizontal space
4. **Vertical Stretch** - Priority for vertical space
5. **Control Type** - Widget type hint (optional)

---

## Policy Types

### 1. Fixed
```python
QSizePolicy.Policy.Fixed
```
- **Behavior**: Widget cannot grow or shrink
- **Size**: Uses `sizeHint()` only
- **Use Case**: Buttons, icons, labels with fixed dimensions
- **Example**:
  ```python
  button = QPushButton("OK")
  button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
  button.setFixedSize(100, 30)
  ```

### 2. Minimum
```python
QSizePolicy.Policy.Minimum
```
- **Behavior**: Can grow, cannot shrink below `sizeHint()`
- **Size**: `sizeHint()` is minimum size
- **Use Case**: Labels that need to grow but maintain minimum width
- **Example**:
  ```python
  label = QLabel("Username:")
  label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
  ```

### 3. Maximum
```python
QSizePolicy.Policy.Maximum
```
- **Behavior**: Can shrink, cannot grow beyond `sizeHint()`
- **Size**: `sizeHint()` is maximum size
- **Use Case**: Widgets that should compress when space is limited
- **Example**:
  ```python
  spacer = QWidget()
  spacer.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
  ```

### 4. Preferred
```python
QSizePolicy.Policy.Preferred
```
- **Behavior**: Can grow and shrink, prefers `sizeHint()`
- **Size**: `sizeHint()` is preferred size
- **Use Case**: Default for most widgets, balanced resizing
- **Example**:
  ```python
  text_edit = QTextEdit()
  text_edit.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
  ```

### 5. Expanding
```python
QSizePolicy.Policy.Expanding
```
- **Behavior**: Can grow and shrink, wants to grow
- **Size**: Uses `sizeHint()` but claims extra space
- **Use Case**: Main content areas, text editors
- **Example**:
  ```python
  text_browser = QTextBrowser()
  text_browser.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
  ```

### 6. MinimumExpanding
```python
QSizePolicy.Policy.MinimumExpanding
```
- **Behavior**: Cannot shrink below `sizeHint()`, wants to grow
- **Size**: `sizeHint()` is minimum, wants more space
- **Use Case**: Rare, similar to Expanding with strict minimum
- **Example**:
  ```python
  widget = QWidget()
  widget.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
  ```

### 7. Ignored
```python
QSizePolicy.Policy.Ignored
```
- **Behavior**: Ignores `sizeHint()`, can be any size
- **Size**: No preference, totally flexible
- **Use Case**: Spacers, widgets with no intrinsic size
- **Example**:
  ```python
  spacer = QWidget()
  spacer.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
  ```

---

## Size Policy Properties

### Getting and Setting Policies

```python
# Get current policy
policy = widget.sizePolicy()

# Get individual directions
h_policy = policy.horizontalPolicy()
v_policy = policy.verticalPolicy()

# Set new policy
new_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
widget.setSizePolicy(new_policy)

# Modify existing policy
policy.setHorizontalPolicy(QSizePolicy.Policy.Preferred)
policy.setVerticalPolicy(QSizePolicy.Policy.Expanding)
widget.setSizePolicy(policy)
```

### Additional Properties

```python
# Set whether widget wants to grow
policy.setHorizontalStretch(2)
policy.setVerticalStretch(1)

# Get stretch values
h_stretch = policy.horizontalStretch()
v_stretch = policy.verticalStretch()

# Control type (affects tab order)
policy.setControlType(QSizePolicy.ControlType.PushButton)

# Height for width (widget's height depends on width)
policy.setHeightForWidth(True)
has_hfw = policy.hasHeightForWidth()

# Width for height (widget's width depends on height)
policy.setWidthForHeight(True)
has_wfh = policy.hasWidthForHeight()

# Retain size when hidden
policy.setRetainSizeWhenHidden(True)
```

---

## Stretch Factors

### What are Stretch Factors?

Stretch factors determine how extra space is distributed among widgets in a layout. They work as **ratios**, not absolute values.

### Basic Concept

```python
# Widget A: stretch = 1
# Widget B: stretch = 2
# Widget C: stretch = 1
# Total stretch = 4

# If 400px extra space available:
# Widget A gets: 400 * (1/4) = 100px
# Widget B gets: 400 * (2/4) = 200px
# Widget C gets: 400 * (1/4) = 100px
```

### Setting Stretch in Layouts

#### QHBoxLayout / QVBoxLayout

```python
from PySide6.QtWidgets import QHBoxLayout, QPushButton

layout = QHBoxLayout()

# Add widgets with stretch factors
button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")
button3 = QPushButton("Button 3")

layout.addWidget(button1, 1)  # stretch factor = 1
layout.addWidget(button2, 3)  # stretch factor = 3
layout.addWidget(button3, 1)  # stretch factor = 1

# button2 will be 3x wider than button1 and button3
```

#### Adding Stretch Space

```python
layout = QHBoxLayout()

layout.addWidget(QPushButton("Left"))
layout.addStretch(1)  # Add flexible space
layout.addWidget(QPushButton("Right"))

# Pushes buttons to edges with space between
```

### Stretch vs Size Policy

**Important Distinction:**

```python
# Size Policy Stretch (in widget)
policy = widget.sizePolicy()
policy.setHorizontalStretch(2)
widget.setSizePolicy(policy)

# Layout Stretch (in layout)
layout.addWidget(widget, 2)  # stretch parameter

# Both work together:
# Layout stretch is usually more commonly used
# Size policy stretch is used when widget should claim more space globally
```

### Stretch Factor Examples

#### Example 1: Three-Column Layout
```python
layout = QHBoxLayout()

# Left sidebar (narrow)
sidebar = QWidget()
layout.addWidget(sidebar, 1)

# Main content (wide)
content = QTextEdit()
layout.addWidget(content, 4)

# Right panel (medium)
panel = QWidget()
layout.addWidget(panel, 2)

# Ratio is 1:4:2
# If window is 700px: 100px | 400px | 200px
```

#### Example 2: Toolbar with Spacer
```python
toolbar = QHBoxLayout()

toolbar.addWidget(QPushButton("New"))
toolbar.addWidget(QPushButton("Open"))
toolbar.addWidget(QPushButton("Save"))
toolbar.addStretch()  # Push buttons to left
toolbar.addWidget(QPushButton("Settings"))

# Buttons on left, Settings on right
```

#### Example 3: Centered Widget
```python
layout = QHBoxLayout()

layout.addStretch(1)
layout.addWidget(QPushButton("Centered"), 0)
layout.addStretch(1)

# Equal stretch on both sides centers the button
```

---

## Practical Examples

### Example 1: Form Layout with Labels and Fields

```python
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit

def create_form_row(label_text):
    row = QWidget()
    layout = QHBoxLayout(row)
    
    # Label: fixed width, doesn't grow
    label = QLabel(label_text)
    label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    label.setFixedWidth(100)
    
    # Input: expands to fill space
    input_field = QLineEdit()
    input_field.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
    
    layout.addWidget(label)
    layout.addWidget(input_field)
    
    return row
```

### Example 2: Resizable Splitter-like Layout

```python
from PySide6.QtWidgets import QVBoxLayout, QTextEdit, QListWidget

layout = QVBoxLayout()

# Top area: takes 2/3 of space
text_edit = QTextEdit()
text_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
layout.addWidget(text_edit, 2)

# Bottom area: takes 1/3 of space
list_widget = QListWidget()
list_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
layout.addWidget(list_widget, 1)
```

### Example 3: Button Bar

```python
from PySide6.QtWidgets import QHBoxLayout, QPushButton

button_layout = QHBoxLayout()

# Fixed-size buttons
ok_btn = QPushButton("OK")
ok_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
ok_btn.setFixedWidth(80)

cancel_btn = QPushButton("Cancel")
cancel_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
cancel_btn.setFixedWidth(80)

# Layout
button_layout.addStretch()  # Push buttons to right
button_layout.addWidget(ok_btn)
button_layout.addWidget(cancel_btn)
```

### Example 4: Dashboard Grid

```python
from PySide6.QtWidgets import QGridLayout, QWidget

grid = QGridLayout()

# Create panels with different stretch priorities
panel1 = QWidget()  # Top-left, normal size
panel2 = QWidget()  # Top-right, wider
panel3 = QWidget()  # Bottom, full width

grid.addWidget(panel1, 0, 0)
grid.addWidget(panel2, 0, 1)
grid.addWidget(panel3, 1, 0, 1, 2)  # Span 2 columns

# Column stretches: left column 1, right column 2
grid.setColumnStretch(0, 1)
grid.setColumnStretch(1, 2)

# Row stretches: equal distribution
grid.setRowStretch(0, 1)
grid.setRowStretch(1, 1)
```

---

## Best Practices

### 1. Use Appropriate Policy Types

**DO:**
```python
# Labels: Usually Fixed or Minimum
label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

# Text inputs: Expanding horizontal, Fixed vertical
line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

# Text areas: Expanding both directions
text_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
```

**DON'T:**
```python
# Avoid Expanding for buttons (they look weird when large)
button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)  # Bad
```

### 2. Combine with Size Constraints

```python
# Set minimum size for Expanding widgets
widget.setMinimumSize(200, 100)
widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

# Set maximum size for preventing over-expansion
widget.setMaximumWidth(500)
```

### 3. Use Stretch Factors Wisely

```python
# Use simple ratios (1:2:1 rather than 13:27:15)
layout.addWidget(widget1, 1)
layout.addWidget(widget2, 2)
layout.addWidget(widget3, 1)
```

### 4. Default Policies are Often Fine

```python
# Many widgets have sensible defaults
# Only override when necessary
button = QPushButton("Click")  # Default is already good

# Only change when you need specific behavior
custom_widget = MyWidget()
custom_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
```

### 5. Test with Window Resizing

Always test your layouts by:
- Resizing the window to minimum size
- Expanding to maximum size
- Testing intermediate sizes
- Checking different aspect ratios

---

## Common Patterns

### Pattern 1: Sidebar Layout

```python
main_layout = QHBoxLayout()

# Sidebar: fixed width or minimum width
sidebar = QListWidget()
sidebar.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
sidebar.setMinimumWidth(200)
sidebar.setMaximumWidth(300)

# Main area: takes remaining space
content = QTextEdit()
content.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

main_layout.addWidget(sidebar, 1)
main_layout.addWidget(content, 4)
```

### Pattern 2: Dialog with Button Bar

```python
dialog_layout = QVBoxLayout()

# Content area: expandable
content = QWidget()
content.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
dialog_layout.addWidget(content)

# Button bar: fixed height, buttons on right
button_bar = QHBoxLayout()
button_bar.addStretch()
button_bar.addWidget(QPushButton("OK"))
button_bar.addWidget(QPushButton("Cancel"))

dialog_layout.addLayout(button_bar)
```

### Pattern 3: Responsive Form

```python
form_layout = QVBoxLayout()

for field_name in ["Name", "Email", "Phone"]:
    row = QHBoxLayout()
    
    label = QLabel(field_name + ":")
    label.setFixedWidth(80)
    
    field = QLineEdit()
    field.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
    
    row.addWidget(label)
    row.addWidget(field)
    
    form_layout.addLayout(row)

form_layout.addStretch()  # Push fields to top
```

### Pattern 4: Status Bar with Sections

```python
status_layout = QHBoxLayout()

# Left section: expanding label
left_label = QLabel("Ready")
left_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
status_layout.addWidget(left_label, 3)

# Middle section: fixed label
middle_label = QLabel("Items: 0")
middle_label.setFixedWidth(100)
status_layout.addWidget(middle_label, 0)

# Right section: fixed label
right_label = QLabel("Status: OK")
right_label.setFixedWidth(120)
status_layout.addWidget(right_label, 0)
```

---

## Advanced Topics

### Height for Width

Some widgets need their height to depend on their width (like word-wrapped labels):

```python
label = QLabel("Long text that will wrap...")
label.setWordWrap(True)

policy = label.sizePolicy()
policy.setHeightForWidth(True)
label.setSizePolicy(policy)

# Override sizeHint if creating custom widget
def hasHeightForWidth(self):
    return True

def heightForWidth(self, width):
    # Calculate height based on width
    return calculated_height
```

### Custom Size Hints

```python
class CustomWidget(QWidget):
    def sizeHint(self):
        # Preferred size
        return QSize(200, 100)
    
    def minimumSizeHint(self):
        # Minimum usable size
        return QSize(100, 50)
```

### Size Policy with QGridLayout

```python
grid = QGridLayout()

# Set column stretches
grid.setColumnStretch(0, 1)  # Left column
grid.setColumnStretch(1, 3)  # Middle column (3x wider)
grid.setColumnStretch(2, 1)  # Right column

# Set row stretches
grid.setRowStretch(0, 1)  # Top row
grid.setRowStretch(1, 2)  # Bottom row (2x taller)

# Add widgets
grid.addWidget(widget1, 0, 0)  # Top-left
grid.addWidget(widget2, 0, 1)  # Top-middle
grid.addWidget(widget3, 1, 0, 1, 3)  # Bottom, spans all columns
```

---

## Quick Reference Table

| Policy | Can Grow | Can Shrink | Prefers Growth | Use Case |
|--------|----------|------------|----------------|----------|
| **Fixed** | ❌ | ❌ | ❌ | Buttons, icons |
| **Minimum** | ✅ | ❌ | ❌ | Labels, minimum size widgets |
| **Maximum** | ❌ | ✅ | ❌ | Collapsible sections |
| **Preferred** | ✅ | ✅ | ❌ | Default, balanced widgets |
| **Expanding** | ✅ | ✅ | ✅ | Text editors, main content |
| **MinimumExpanding** | ✅ | ❌ | ✅ | Rare, strict minimum |
| **Ignored** | ✅ | ✅ | ❌ | Spacers, totally flexible |

---

## Summary

### Key Takeaways

1. **Size Policy** controls how widgets resize
2. **Stretch Factors** control proportional space distribution
3. Use **Fixed** for buttons and icons
4. Use **Expanding** for main content areas
5. Use **stretch factors** in layouts for proportional sizing
6. Always test layouts by resizing windows
7. Combine size policies with min/max size constraints
8. Default policies are often sufficient

### Common Combinations

```python
# Button
button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

# Text Input (single line)
line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

# Text Editor (multi-line)
text_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

# Label (fixed text)
label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

# Label (variable text)
label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

# Spacer
spacer = QWidget()
spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
```

---

## Resources

- **Official Documentation**: [Qt Size Policy](https://doc.qt.io/qt-6/qsizepolicy.html)
- **Layout Management**: [Qt Layout Classes](https://doc.qt.io/qt-6/layout.html)
- **Widget Sizing**: [Qt Widget Geometry](https://doc.qt.io/qt-6/qwidget.html#size-hints-and-size-policies)

---

*This guide covers the theoretical foundations of size policies and stretches in PySide6. Practice with real examples to master responsive GUI design!*
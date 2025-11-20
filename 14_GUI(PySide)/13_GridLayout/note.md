# QGridLayout — Theoretical Notes

## Overview
QGridLayout is a layout manager in Qt used to arrange widgets in a two-dimensional grid structure made of rows and columns. It provides a flexible and organized way to position widgets, especially when alignment and spacing matter.

## Key Concepts

### Grid Structure
- Widgets are placed at specific **row** and **column** positions.
- Each cell in the grid can contain one widget.
- A widget can span multiple **rows** or **columns**.

### Stretch Factors
- Stretch factors control how additional space is distributed across rows and columns.
- Higher stretch factor → that row/column grows more when the window resizes.

### Spacing & Margins
- **Spacing** refers to the space between widgets.
- **Contents margins** refer to the space between the layout and the window/widget boundary.
- Both can be customized for precise control.

### Alignment
- Widgets placed in the grid can be aligned (left, right, top, bottom, center).
- Alignment ensures widgets appear consistently even when the layout stretches.

### Size Policies
- QGridLayout respects each widget’s **size policy**, **minimum size**, and **size hint**.
- Layout adjusts sizes proportionally based on these properties.

### Ownership & Parenting
- When a QGridLayout is set on a parent widget, it automatically manages the widgets added to it.
- Memory management is handled by Qt; deleting the parent deletes the layout and child widgets.

### Layout Management Rules
- QGridLayout recalculates and updates widget positions when:
  - The parent widget is resized.
  - A widget’s size policy or size hint changes.
  - The layout structure (rows, columns, spans) is modified.

### Use Cases
- Creating structured forms.
- Organizing widgets in rows and columns.
- Interfaces requiring symmetric and clean alignment.
- Dynamic layouts that adapt to resizing.

## Advantages
- Intuitive row/column positioning.
- Very flexible for responsive UI layout.
- Supports row/column spanning.
- Automatically handles widget resizing and alignment.

## Limitations
- Complex UIs may require combining with other layouts.
- Not ideal for highly free-form or irregular widget placement.
- Requires careful row/column planning for aesthetic balance.

## Common Operations (Conceptual Only)
- Adding widgets to specific grid positions.
- Setting row/column stretch.
- Adjusting spacing and margins.
- Controlling alignment.
- Managing spanning across multiple cells.
# QTabWidget — Theoretical Notes (PySide6)

## Overview
`QTabWidget` is a container widget in Qt that organizes content into multiple pages, each accessible via tabs. It allows users to switch between different views within the same window.

## Purpose
- To group related content into separate sections.
- To provide a navigable interface without using multiple windows.
- To improve UI organization by dividing content logically.

## Key Concepts

### Tabs
- Each page added to a `QTabWidget` appears as a tab at the top (or optionally bottom, left, or right).
- Tabs display a label and can optionally include icons or tooltips.
- Tabs can be made closable or movable depending on the configuration.

### Pages (Widgets)
- Each tab corresponds to a widget that is displayed when the tab is selected.
- Any QWidget-based element can serve as a page.

### Current Index
- `QTabWidget` maintains an internal index that represents which tab/page is currently active.
- The index changes whenever the user clicks a different tab.

### Tab Position
- Tabs can be positioned: North (top), South (bottom), West (left), East (right).

### Tab Shape
- Tabs can have shapes such as rounded or triangular.
- Shape is mainly visual but affects UI style consistency.

### Signals
- Signals are emitted when user interaction changes the selected tab.
- Useful for updating the UI or handling logic based on selected content.

### Tab Control Features
- Tabs can be enabled or disabled individually.
- Tabs can be made closable via a close button.
- Tabs can be renamed dynamically.
- Reordering can be allowed through movable tabs.

### Styling
- Tabs and pages can be styled using Qt Style Sheets for custom UI themes.
- Styling can target the tab bar, individual tabs, or the content area.

### Integration
- `QTabWidget` internally uses a `QTabBar` for the actual tabs and a stack-like container for pages.
- It can be placed anywhere in layouts and combined with other widgets.

## Use Cases
- Settings or preferences dialogs.
- Multi-page forms.
- Interfaces with multiple views such as editors, dashboards, or tools.
- Organizing related but separate functional components.
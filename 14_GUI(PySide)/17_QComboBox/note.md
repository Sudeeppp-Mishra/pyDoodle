# QComboBox

## Introduction
`QComboBox` is a widget provided by the Qt framework that allows users to select one option from a drop-down list. It is commonly used in graphical user interfaces when space is limited and a predefined set of choices must be presented.

## Features of QComboBox
- Displays a list of selectable items in a drop-down menu
- Allows selection of only one item at a time
- Supports both editable and non-editable modes
- Can store associated user data with each item
- Provides signals to detect selection changes

## Modes of QComboBox
- **Non-editable ComboBox**: User can only select items from the list
- **Editable ComboBox**: User can type custom text in addition to selecting items

## Commonly Used Functions
- `addItem(text)` – Adds a single item to the combo box
- `addItems(list)` – Adds multiple items at once
- `currentText()` – Returns the currently selected text
- `currentIndex()` – Returns the index of the selected item
- `setCurrentIndex(index)` – Sets the selected item by index
- `setEditable(bool)` – Enables or disables text editing

## Signals
- `currentIndexChanged` – Emitted when the selected index changes
- `currentTextChanged` – Emitted when the selected text changes
- `activated` – Emitted when the user selects an item

## Applications of QComboBox
- Selecting country, gender, or category
- Choosing settings or preferences
- Filtering data in applications
- Form inputs with predefined values

## Advantages
- Saves screen space
- Easy to use and implement
- Improves user experience by limiting input errors
- Supports dynamic item insertion

## Conclusion
`QComboBox` is a flexible and efficient widget in Qt used for presenting a list of selectable options. It enhances usability and ensures structured input in desktop applications.
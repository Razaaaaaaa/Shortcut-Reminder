# Shortcut Reminder POC 

Prototype exploring the use of AT-SPI (Assistive Technology Service Provider Interface) to implement a shortcut reminder.

## Objective

Investigate whether AT-SPI can be used to detect relevant application events and provide contextual reminders for keyboard shortcuts.

## selection.py

- [x] `Ctrl+A` → Select all
- [x] `Shift+Left` → Select previous character
- [x] `Shift+Right` → Select next character
- [x] `Shift+Up` → Select previous line
- [x] `Shift+Down` → Select next line
- [x] `Shift+Home` → Select to the beginning of the line
- [x] `Shift+End` → Select to the end of the line
- [x] `Ctrl+Shift+Left` → Select previous word
- [x] `Ctrl+Shift+Right` → Select next word
- [x] `Ctrl+Shift+Home` → Select to the beginning of the document
- [x] `Ctrl+Shift+End` → Select to the end of the document

## navigation.py

- [ ] `Left` → Previous character
- [ ] `Right` → Next character
- [ ] `Up` → Previous line
- [ ] `Down` → Next line
- [ ] `Home` → Beginning of line
- [ ] `End` → End of line
- [ ] `Ctrl+Left` → Previous word
- [ ] `Ctrl+Right` → Next word
- [ ] `Ctrl+Up` → Previous paragraph
- [ ] `Ctrl+Down` → Next paragraph
- [ ] `Ctrl+Home` → Beginning of text
- [ ] `Ctrl+End` → End of text
- [ ] `PageUp` → Previous page
- [ ] `PageDown` → Next page

## editing.py

- [ ] `Backspace` → Delete before the cursor
- [ ] `Delete` → Delete after the cursor
- [ ] `Ctrl+Backspace` → Delete previous word
- [ ] `Ctrl+Delete` → Delete next word
- [ ] `Enter` → New line / confirm
- [ ] `Tab` → Tab / move to the next field
- [ ] `Shift+Tab` → Move to the previous field

## clipboard.py

- [ ] `Ctrl+C` → Copy
- [ ] `Ctrl+X` → Cut
- [ ] `Ctrl+V` → Paste
- [ ] `Ctrl+Shift+V` → Paste without formatting, depending on the application
- [ ] `Ctrl+A` → Select all

## undo-redo.py

- [ ] `Ctrl+Z` → Undo
- [ ] `Ctrl+Y` → Redo
- [ ] `Ctrl+Shift+Z` → Redo, depending on the application

## search.py

- [ ] `Ctrl+F` → Find
- [ ] `Ctrl+H` → Find and replace, depending on the application
- [ ] `Ctrl+G` → Find next occurrence, depending on the application
- [ ] `Ctrl+Shift+G` → Find previous occurrence, depending on the application

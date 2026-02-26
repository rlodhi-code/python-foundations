# **Tkinter Exercises (GUI Practice Collection)**

A collection of small Tkinter programs demonstrating core GUI concepts in Python. These exercises cover labels, buttons, entry widgets, text boxes, spinboxes, scales, checkbuttons, radiobuttons, listboxes, and simple event‑driven callbacks. The folder also includes a standalone miles‑to‑kilometers converter and a short playground script illustrating `*args`, `**kwargs`, and class initialization patterns.

---

## 🧩 Contents

### **1. main.py — Basic GUI Layout and Interaction**
A simple interface demonstrating:

- Creating a window with padding and minimum size  
- Labels with custom fonts and padding  
- Buttons triggering callback functions  
- Entry widget for user input  
- Grid‑based layout  

**Key behavior:**  
Clicking the button prints a message and updates the label with the text from the entry field.

---

### **2. miles_to_km_converter.py — Unit Conversion App**
A compact GUI tool that converts miles to kilometers.

Features:

- Entry field for numeric input  
- Labels for units and results  
- Button that triggers the conversion  
- Simple arithmetic using the formula:  
  \[
  \text{km} = \text{miles} \times 1.60934
  \]

This script demonstrates how to read user input, perform calculations, and update the interface dynamically.

---

### **3. other_tkinter_widgets.py — Widget Demonstration Panel**
A comprehensive showcase of Tkinter widgets and event handling:

- **Label** — updating text  
- **Button** — calling a function  
- **Entry** — inserting and retrieving text  
- **Text** — multi‑line input  
- **Spinbox** — numeric selection with callback  
- **Scale** — slider with live value updates  
- **Checkbutton** — boolean state tracking  
- **Radiobutton** — mutually exclusive options  
- **Listbox** — item selection with event binding  

This script provides a broad overview of Tkinter’s core widget set and how to interact with user‑generated events.

---

### **4. playground.py — Python Argument Patterns**
A non‑GUI script demonstrating:

- `*args` for variable‑length positional arguments  
- `**kwargs` for variable‑length keyword arguments  
- Safe dictionary access using `.get()`  
- A simple `Car` class that accepts flexible initialization parameters  

This file supports understanding of Python fundamentals often used in GUI callbacks and configuration.

---

## 📁 Project Structure

```
tkinter-exercises/
│
├── main.py
├── miles_to_km_converter.py
├── other_tkinter_widgets.py
└── playground.py
```

---

## 🖥️ Running Any Script

Each file is standalone. Run any exercise with:

```
python filename.py
```

Tkinter is included with standard Python installations.

---

## 🚀 Extensions to Explore

- Add themes or color schemes  
- Combine multiple widgets into a single application  
- Add validation for numeric inputs  
- Create reusable widget classes  
- Build a small multi‑page Tkinter app using frames  

---


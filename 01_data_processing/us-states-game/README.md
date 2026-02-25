# 🇺🇸 US States Game  
A Python-based interactive geography quiz using **turtle graphics**, **pandas**, and **Tkinter** message boxes. Players try to name all 50 U.S. states, and the game displays each correctly guessed state on a blank U.S. map.

---

## 📌 Project Overview
This project recreates a classic U.S. geography quiz. The user is shown a blank map of the United States and is prompted to guess state names. When a correct guess is entered:

- The state name is written on the map at its correct coordinates  
- The guess is recorded  
- The score updates in the window title  

When the user types **Exit**, or when all 50 states are guessed, the game ends and a file is generated listing any states the user missed.

---

## 🗂️ Folder Contents

| File | Description |
|------|-------------|
| `main.py` | Main game script using turtle graphics and pandas. |
| `50_states.csv` | Dataset containing each state’s name and its (x, y) coordinates on the map. |
| `blank_states_img.gif` | Background image of the U.S. map used by the turtle screen. |
| `missed_states.csv` | Auto-generated file listing states the user did not guess. |

---

## 🧠 How the Game Works

1. The program loads a blank U.S. map (`blank_states_img.gif`).
2. It reads `50_states.csv`, which contains:
   - `state` — the state name  
   - `x`, `y` — coordinates for placing the label on the map
3. A popup welcomes the player.
4. The game repeatedly prompts the user to enter a state name.
5. For each correct guess:
   - A turtle writes the state name at the correct location.
   - The guess is added to a set of completed states.
6. If the user enters **Exit**, the game stops early.
7. At the end, the program creates `missed_states.csv` containing all unguessed states.

---

## 📊 Example of `50_states.csv`

```
state,x,y
Alabama,139,-77
Alaska,-204,-170
Arizona,-203,-40
...
Wyoming,-134,90
```

Each row maps a state to its position on the background image.

---

## ▶️ Running the Game

### **Requirements**
- Python 3.x  
- `pandas`  
- `tkinter` (included with most Python installations)  
- `turtle` (included with Python)

### **Install dependencies**
```bash
pip install pandas
```

### **Run the script**
```bash
python main.py
```

A window will open with the U.S. map and prompt you to begin guessing.

---

## 📁 Output File

After the game ends, the script generates:

### `missed_states.csv`
A simple list of states the user did not guess:

```
Missed States
Nevada
Vermont
...
```

This is useful for studying or reviewing missed answers.

---

## 🎯 Learning Objectives

This project helps reinforce:

- Reading CSV files with **pandas**
- Using **turtle graphics** for interactive programs
- Handling user input with **Tkinter** dialogs
- Writing data back to CSV
- Basic game logic and loops
- Coordinate-based drawing

---

## 🙌 Credits
This project is part of the **Python Foundations** learning series.

---


# **Flash Cards App (Tkinter GUI)**

A simple, interactive flash‑card application built with **Python**, **Tkinter**, and **Pandas**.  
The app helps users learn French vocabulary using spaced‑repetition–style behavior:  
unknown words reappear, and known words are removed from the learning list.

---

## 🎯 **Features**

- **Flash‑card interface** with front/back flipping animation  
- **Auto‑flip timer** (3 seconds) from French → English  
- **Persistent progress tracking** using `words_to_learn.csv`  
- **Randomized card selection**  
- **Clean Tkinter UI** with images and buttons  
- **Beginner‑friendly code structure**  

---

## 📁 **Project Structure**

```
flash-cards-app/
│
├── main.py
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv   # auto‑generated after first run
│
└── images/
    ├── card_front.png
    ├── card_back.png
    ├── right.png
    └── wrong.png
```

---

## 🚀 **How It Works**

### 1. **Load vocabulary**
- On first run, the app loads `french_words.csv`.
- After you mark words as *known*, the app saves remaining words to `words_to_learn.csv`.
- On future runs, the app loads from `words_to_learn.csv` to continue where you left off.

### 2. **Show a random French word**
- A card appears with the French word.
- After 3 seconds, the card flips to show the English translation.

### 3. **User actions**
- **✔️ Known** → removes the word from the learning list and updates the CSV  
- **❌ Unknown** → keeps the word in the list and moves to the next card  

---

## 🧠 **Core Logic Overview**

### **Selecting the next card**
```python
current_card = random.choice(to_learn)
canvas.itemconfig(card_title, text="French")
canvas.itemconfig(card_word, text=current_card["French"])
```

### **Flipping the card**
```python
canvas.itemconfig(card_title, text="English")
canvas.itemconfig(card_word, text=current_card["English"])
```

### **Saving progress**
```python
to_learn.remove(current_card)
pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
```

---

## 🖥️ **Running the App**

### **Prerequisites**
- Python 3.10+
- Required libraries:
  ```
  pandas
  tkinter (bundled with Python)
  ```

### **Run**
```
python main.py
```

---

## 📊 **Dataset**

The app uses a simple CSV file with two columns:

```
French,English
partie,part
histoire,history
chercher,search
...
```

You can replace this dataset with your own language pairs to create custom flash‑card sets.

---

## 🧩 **Possible Extensions**

- Add progress bar or statistics  
- Add multiple language decks  
- Add audio pronunciation  
- Add dark mode  
- Add spaced‑repetition algorithm (SM‑2)  

---


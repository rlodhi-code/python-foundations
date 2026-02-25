# 🔤 NATO Phonetic Alphabet Generator  
A simple command‑line application that converts any word into its **NATO phonetic alphabet** equivalent. This project demonstrates how to read CSV data with **pandas**, build dictionaries efficiently, handle user input, and manage errors gracefully.

---

## 📌 Project Overview
This CLI tool takes a user‑entered word and translates each letter into its corresponding **NATO phonetic code word** (e.g., “A → Alfa”, “B → Bravo”). It is a clean, beginner‑friendly example of:

- Reading CSV files with pandas  
- Iterating through DataFrame rows  
- Building dictionaries using dictionary comprehensions  
- Handling invalid input with exceptions  
- Recursively prompting the user until valid input is provided  

---

## 🗂️ Folder Contents

| File | Description |
|------|-------------|
| `main.py` | Main script that loads the NATO alphabet and generates phonetic translations. |
| `nato_phonetic_alphabet.csv` | Dataset containing letters A–Z and their NATO code words. |

---

## 📄 Dataset Details

### **nato_phonetic_alphabet.csv**
This CSV maps each letter to its NATO phonetic alphabet code:

```
letter,code
A,Alfa
B,Bravo
C,Charlie
D,Delta
E,Echo
F,Foxtrot
G,Golf
H,Hotel
I,India
J,Juliet
K,Kilo
L,Lima
M,Mike
N,November
O,Oscar
P,Papa
Q,Quebec
R,Romeo
S,Sierra
T,Tango
U,Uniform
V,Victor
W,Whiskey
X,X-ray
Y,Yankee
Z,Zulu
```

---

## 🧪 How the Script Works

### **1. Load the CSV**
```python
data = pandas.read_csv("nato_phonetic_alphabet.csv")
```

### **2. Build a dictionary**
A dictionary comprehension converts the DataFrame into a lookup table:

```python
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
```

### **3. Prompt the user**
The user enters a word, which is converted to uppercase:

```python
word = input("Enter a word: ").upper()
```

### **4. Generate the phonetic list**
Each letter is mapped to its NATO code:

```python
output_list = [phonetic_dict[letter] for letter in word]
```

### **5. Handle invalid characters**
If the user enters numbers or symbols, a `KeyError` is raised and the user is prompted again:

```python
except KeyError:
    print("Sorry, only letters in the alphabet please.")
    generate_phonetic()
```

---

## ▶️ Running the Application

### **Requirements**
- Python 3.x  
- `pandas`  

Install pandas:

```bash
pip install pandas
```

### **Run the script**
```bash
python main.py
```

Example interaction:

```
Enter a word: Code
['Charlie', 'Oscar', 'Delta', 'Echo']
```

---

## 🎯 Learning Objectives

This project reinforces:

- Reading CSV files with pandas  
- Using dictionary comprehensions  
- Handling exceptions  
- Building simple CLI applications  
- Recursion for repeated user prompts  

These skills form a strong foundation for more advanced data processing and command‑line tools.

---

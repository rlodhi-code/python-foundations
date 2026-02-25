# 🔐 Password Manager v2  
A more advanced version of the Password Manager application, now featuring **search functionality**, **JSON‑based storage**, and improved data handling. This Tkinter GUI tool allows users to generate secure passwords, save them in a structured format, and quickly retrieve stored credentials.

---

## 📌 What’s New in Version 2
Compared to Password Manager v1, this version introduces:

### **✔ JSON storage (`data.json`)**  
Credentials are stored in a structured, nested JSON format instead of plain text.

### **✔ Search functionality**  
Users can enter a website name and instantly retrieve the saved email and password.

### **✔ Improved data handling**  
- Automatically creates `data.json` if it doesn’t exist  
- Merges new entries with existing data  
- Provides clear error messages when data is missing  

---

## 🗂️ Folder Contents

| File | Description |
|------|-------------|
| `main.py` | Main Tkinter application with password generation, saving, and search features. |
| `logo.png` | Application logo displayed at the top of the UI. |
| `data.json` | (Created at runtime) Stores website credentials in JSON format. |

---

## 🧪 Features & How They Work

### **1. Password Generator**
Creates a randomized password using:
- Uppercase and lowercase letters  
- Numbers  
- Symbols  

The password is:
- Inserted directly into the password field  
- Automatically copied to the clipboard via `pyperclip`  

```python
password_letters = [choice(letters) for _ in range(randint(8, 10))]
password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
```

---

### **2. Saving Passwords to JSON**
When the user clicks **Add**, the app:

1. Validates that website and password fields are not empty  
2. Loads existing data from `data.json`  
3. Updates it with the new entry  
4. Saves the merged result back to the file  

Example JSON structure:

```json
{
    "amazon.com": {
        "email": "user@example.com",
        "password": "aB3!xP9&"
    },
    "github.com": {
        "email": "dev@example.com",
        "password": "Xy7#Lm2!"
    }
}
```

If `data.json` doesn’t exist, it is created automatically.

---

### **3. Searching for Saved Credentials**
The **Search** button allows users to retrieve saved credentials instantly.

The app:
- Loads `data.json`
- Checks if the website exists
- Displays the stored email and password in a messagebox

If the file is missing or the website isn’t found, the user receives a clear error message.

---

## 🖥️ User Interface

The UI is built with Tkinter and includes:

- A centered logo  
- Input fields for website, email, and password  
- Buttons for **Search**, **Generate Password**, and **Add**  
- Clean layout using `.grid()`  

---

## ▶️ Running the Application

### **Requirements**
- Python 3.x  
- `pyperclip`  

Install dependencies:

```bash
pip install pyperclip
```

### **Run the app**
```bash
python main.py
```

The window will open with the logo and input fields.

---

## 🎯 Learning Objectives

This project reinforces:

- GUI development with Tkinter  
- JSON file handling  
- Exception handling (`try` / `except` / `else` / `finally`)  
- Clipboard integration  
- Data validation and user feedback  
- Building scalable, maintainable GUI applications  

---


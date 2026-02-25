# 🔐 Password Manager v1  
A beginner‑friendly **Tkinter GUI application** that generates secure passwords and stores them locally. This project demonstrates GUI layout, input handling, file writing, message dialogs, and basic password‑generation logic. It also includes clipboard integration for quick copying.

---

## 📌 Project Overview
This application provides three core features:

### **1. Password Generation**
Creates a randomized password using:
- Uppercase and lowercase letters  
- Numbers  
- Symbols  

The generated password is:
- Inserted directly into the password field  
- Automatically copied to the clipboard via `pyperclip`  

### **2. Data Entry Form**
Users can enter:
- Website  
- Email/Username  
- Password  

The UI is built with **Tkinter**, using labels, entry fields, buttons, and a canvas for the logo.

### **3. Local Storage**
When the user clicks **Add**, the app:
- Validates that required fields are not empty  
- Asks for confirmation via a messagebox  
- Saves the entry to `data.txt` in the format:  
  ```
  website | email | password
  ```

---

## 🗂️ Folder Contents

| File | Description |
|------|-------------|
| `main.py` | Main Tkinter application containing UI, password generator, and save logic. |
| `logo.png` | Application logo displayed at the top of the UI. |
| `data.txt` | (Created at runtime) Stores saved website credentials. |

---

## 🧪 How the Application Works

### **Password Generator**
The generator creates a password by selecting:
- 8–10 random letters  
- 2–4 random symbols  
- 2–4 random numbers  

Then it shuffles them and joins them into a final string:

```python
password_letters = [choice(letters) for _ in range(randint(8, 10))]
password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

password_list = password_letters + password_symbols + password_numbers
shuffle(password_list)
password = "".join(password_list)
```

The password is:
- Inserted into the password entry field  
- Copied to the clipboard automatically  

---

### **Saving Passwords**
The `save()` function:

1. Reads values from the entry fields  
2. Ensures website and password are not empty  
3. Displays a confirmation dialog  
4. Appends the entry to `data.txt`  
5. Clears the website and password fields  

Example saved line:

```
amazon.com | user@example.com | aB3!xP9&
```

---

## 🖥️ User Interface

The UI is built with Tkinter and includes:

- A centered logo  
- Input fields for website, email, and password  
- A **Generate Password** button  
- An **Add** button to save credentials  

The layout uses `.grid()` for clean alignment.

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

- Building GUIs with Tkinter  
- Using message boxes for alerts and confirmations  
- Generating random passwords  
- Writing to files  
- Using the clipboard programmatically  
- Organizing GUI layouts with `.grid()`  
- Handling user input and validation  

These skills form a strong foundation for more advanced GUI applications and password‑management tools.

---

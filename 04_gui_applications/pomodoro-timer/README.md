# **Pomodoro Timer (Tkinter GUI)**

A clean, customizable Pomodoro productivity timer built with **Python** and **Tkinter**. The app cycles through focused work sessions and short/long breaks, visually tracks progress with check marks, and prevents accidental multiple-timer starts.

---

## ⏱️ Purpose

The Pomodoro technique improves focus by breaking work into timed intervals. This app automates the cycle:

- Work session  
- Short break  
- Work session  
- Short break  
- …  
- Long break after every 4 work sessions  

Your version includes adjustable durations for testing and a session‑completion indicator.

---

## 🧩 Features

- Automatic cycling through **work**, **short break**, and **long break** intervals  
- **Start** and **Reset** controls  
- **Timer‑running lock** to prevent duplicate timers  
- **Check‑mark progress tracking** after each completed work session  
- **Session completion detection** after a configurable number of cycles  
- Clean Tkinter UI with a tomato graphic  
- Easy to customize durations for real use or testing  

---

## 📁 Project Structure

```
pomodoro-timer/
│
├── main.py
└── tomato.png
```

---

## ⚙️ How It Works

### Timer flow
The app uses a repetition counter (`reps`) to determine which phase to run:

- `reps % 8 == 0` → long break  
- `reps % 2 == 0` → short break  
- otherwise → work session  

### Preventing multiple timers
A global flag ensures only one countdown runs at a time:

```python
if timer_running:
    return
timer_running = True
```

### Countdown mechanism
The timer updates every second using Tkinter’s `after()`:

```python
timer = window.after(1000, count_down, count - 1)
```

### Reset behavior
Reset cancels the active timer, clears the UI, resets counters, and restores the Start button.

---

## 🖥️ Running the App

### Requirements
- Python 3.10+
- Tkinter (included with Python)

### Run
```
python main.py
```

---

## 🎨 UI Overview

- Tomato image centered on a canvas  
- Large timer text overlay  
- Start and Reset buttons  
- Check marks displayed below the timer  

---

## 🔧 Configuration

You can adjust durations at the top of `main.py`:

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOTAL_WORK_SESSIONS = 6
```

For testing, the values are set to 1–2 minutes.

---

## 🚀 Possible Enhancements

- Add sound notifications  
- Add pause/resume  
- Add statistics dashboard  
- Add theme switching (dark/light)  
- Add system tray mode  

---


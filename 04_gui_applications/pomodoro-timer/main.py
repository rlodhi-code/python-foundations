from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1 #5
LONG_BREAK_MIN = 2 #20
TOTAL_WORK_SESSIONS = 6

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
timer = None          # stores the after() id so we can cancel it
timer_running = False # prevents multiple timers
reps = 0
# ---------------------------- TIMER START ------------------------------- #
def start_timer():
    global timer_running

    if timer_running:
        return  # ← prevents starting another timer

    timer_running = True
    start_button.config(state="disabled", text="Running…")
    # For testing — start with 5 seconds
    # In real Pomodoro: count_down(WORK_MIN * 60)
    # count_down(WORK_MIN * 60)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, timer_running
    # Cancel any running timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None

    timer_running = False
    # Reset display
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    start_button.config(state="normal", text="Start")
    ## remove check marks
    check_marks.configure(text="", fg=GREEN, bg=YELLOW)
    # check_marks.grid(row=3, column=1)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def count_down(count):
    global timer, timer_running
    # Convert count (in seconds) to minutes and seconds

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_running = False
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
        if work_sessions >= TOTAL_WORK_SESSIONS:
            title_label.config(text="Complete!", fg=GREEN)
            # start_button.config(state="normal", text="Reset to begin")
            start_button.config(state="normal", text="Start")
        else:
            start_timer()
    """
    minutes = count // 60
    seconds = count % 60

    # Format as MM:SS (always show two digits)
    time_text = f"{minutes:02d}:{seconds:02d}"

    # Update the text on the canvas
    canvas.itemconfig(timer_text, text=time_text)

    if count > 0:
        # Schedule the next call after 1000ms (1 second)
        timer = window.after(1000, count_down, count - 1)
    else:
        # Timer has finished — you can add sound, change color, start next phase, etc.
        print("Time's up!")
        timer_running = False
        start_button.config(state="normal", text="Start")
"""
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro (tomato)")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# count_down(5 * 60)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()

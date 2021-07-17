from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_BOX = "✓"

seconds = 60
mins = 0
repetitions = 0

MINS_TIMER = 1
SECONDS_TIMER = "00"
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    total_seconds = MINS_TIMER*60 - mins
    count_down(total_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global seconds, mins
    seconds -= 1
    if seconds < 0:
        mins -= 1
        seconds = 59
    text = f"{mins}:{seconds}"
    if seconds < 10:
        text = f"{mins}:0{seconds}"

    canvas.itemconfig(timer_text, text = text)
    if (count > 0):
        window.after(100, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Work Timer")
window.config(padx = 50, pady = 50, bg = YELLOW)

label_timer = Label(text = "Timer")
label_timer.config(font = (FONT_NAME,30, "bold"), fg = GREEN, bg = YELLOW)
label_timer.grid(row = 0,column = 1)

timer_image = PhotoImage(file ="tomato.png")
canvas = Canvas(width= 200, height = 224, bg = YELLOW, highlightthickness = 0)

canvas.create_image((100,112), image = timer_image)
timer_text = canvas.create_text((100, 130) , text = f"{MINS_TIMER}:{SECONDS_TIMER}", fill = "white", font = (FONT_NAME, 30, "bold"))
canvas.grid(row = 1, column = 1)

start_button = Button(text = "Start", padx = 5, pady = 5, font = FONT_NAME, command = start_timer)
start_button.grid(row = 2,column = 0)

reset_button = Button(text = "Reset", padx = 5, pady = 5, font = FONT_NAME)
reset_button.grid(row = 2, column = 2)

checkbox_label = Label(text = CHECK_BOX, fg = GREEN, font = (FONT_NAME, 20, "bold"), bg = YELLOW)
checkbox_label.grid(row = 3, column = 1)
window.mainloop()
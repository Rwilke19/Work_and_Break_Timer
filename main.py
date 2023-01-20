from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(time)
    check.config(text="")
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")



# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_beak_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(work_sec)
        label.config(text="Work", fg=GREEN)
    if reps == 8:
        countdown(long_beak_sec)
        label.config(text="Long Break", fg=RED)
    if reps == 2 or reps == 4 or reps == 6:
        countdown(short_break_sec)
        label.config(text="Short Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global time
        time = window.after(1000, countdown, count - 1)
    else:
        words = ""
        if reps % 2 == 0:
            words = words + "✔"
            check.config(text=words)
        timer()




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Ketchup")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(row=1, column=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(row=4, column=2)

start = Button(text="Start", command=timer)
start.grid(row=3, column=1)

reset = Button(text="Reset", command=timer_reset)
reset.grid(row=3, column=3)


window.mainloop()
import tkinter as tk
from tkinter import font
from datetime import datetime


def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    clock_label.after(1000, update_clock)


def create_clock_window():
    window = tk.Tk()
    window.title("Digital Clock")
    window.geometry("400x200")
    window.configure(bg='black')

    global clock_label, date_label

    clock_font = font.Font(family='Helvetica', size=80, weight='bold')
    date_font = font.Font(family='Helvetica', size=20, weight='bold')

    clock_label = tk.Label(window, font=clock_font, bg='black', fg='white')
    clock_label.pack(pady=20)

    date_label = tk.Label(window, font=date_font, bg='black', fg='white')
    date_label.pack(pady=10)

    return window


def start_clock():
    window = create_clock_window()
    update_clock()
    window.mainloop()


start_clock()

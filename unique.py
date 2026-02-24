import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random

# ---------------- LOGIN SCREEN ---------------- #

def login():
    if username.get() == "admin" and password.get() == "1234":
        login_frame.pack_forget()
        dashboard_frame.pack(fill="both", expand=True)
    else:
        login_status.config(text="Invalid Credentials", fg="red")

root = tk.Tk()
root.title("Advanced Productivity Dashboard")
root.geometry("800x500")

login_frame = tk.Frame(root)
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="Login",
         font=("Arial", 20, "bold")).pack(pady=20)

username = tk.Entry(login_frame)
username.pack(pady=5)
username.insert(0, "admin")

password = tk.Entry(login_frame, show="*")
password.pack(pady=5)
password.insert(0, "1234")

tk.Button(login_frame, text="Login", command=login).pack(pady=10)
login_status = tk.Label(login_frame, text="")
login_status.pack()

# ---------------- DASHBOARD ---------------- #

dashboard_frame = tk.Frame(root)

# Header
header = tk.Label(dashboard_frame,
                  text="🧠 Productivity Dashboard",
                  font=("Arial", 18, "bold"))
header.pack(pady=10)

# Dark Mode Toggle
is_dark = False

def toggle_mode():
    global is_dark
    if not is_dark:
        dashboard_frame.configure(bg="#1e1e2f")
        header.configure(bg="#1e1e2f", fg="white")
        is_dark = True
    else:
        dashboard_frame.configure(bg="white")
        header.configure(bg="white", fg="black")
        is_dark = False

tk.Button(dashboard_frame,
          text="Toggle Dark Mode",
          command=toggle_mode).pack(pady=5)

# ---------------- TIME ---------------- #

time_label = tk.Label(dashboard_frame, font=("Arial", 12))
time_label.pack()

def update_time():
    now = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=f"Time: {now}")
    root.after(1000, update_time)

update_time()

# ---------------- STATS COUNTER ---------------- #

counter = 0

def increase_counter():
    global counter
    counter += 1
    counter_label.config(text=f"Tasks Completed: {counter}")

counter_label = tk.Label(dashboard_frame,
                         text="Tasks Completed: 0",
                         font=("Arial", 12))
counter_label.pack(pady=5)

tk.Button(dashboard_frame,
          text="Complete Task",
          command=increase_counter).pack(pady=5)

# ---------------- PROGRESS BAR ---------------- #

progress = ttk.Progressbar(dashboard_frame,
                           orient="horizontal",
                           length=300,
                           mode="determinate")
progress.pack(pady=10)

def increase_progress():
    progress["value"] += 10

tk.Button(dashboard_frame,
          text="Increase Progress",
          command=increase_progress).pack(pady=5)

# ---------------- DAILY QUOTE ---------------- #

quotes = [
    "Stay consistent.",
    "Discipline builds freedom.",
    "Small progress daily.",
    "Keep pushing forward.",
    "Focus on growth."
]

def generate_quote():
    quote_label.config(text=random.choice(quotes))

tk.Button(dashboard_frame,
          text="Generate Quote",
          command=generate_quote).pack(pady=5)

quote_label = tk.Label(dashboard_frame,
                       text="Click to get daily quote!",
                       font=("Arial", 12))
quote_label.pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Practice Tracker")
root.geometry("700x500")
root.configure(bg="white")

# ---------------- HEADER ---------------- #
header = tk.Label(root,
                  text="🐍 Python Practice Tracker",
                  font=("Arial", 18, "bold"),
                  bg="#2ecc71",
                  fg="white",
                  height=2)
header.pack(fill=tk.X)

# ---------------- TASK ENTRY ---------------- #
task_frame = tk.Frame(root, bg="white")
task_frame.pack(pady=20)

tk.Label(task_frame, text="Enter Practice Topic:",
         bg="white",
         font=("Arial", 12)).pack()

task_entry = tk.Entry(task_frame, width=40)
task_entry.pack(pady=5)

task_list = []

def add_task():
    task = task_entry.get()
    if task:
        task_list.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

tk.Button(task_frame,
          text="Add Task",
          command=add_task,
          bg="blue", fg="white").pack(pady=5)

# ---------------- TASK LIST ---------------- #
listbox = tk.Listbox(root, width=50, height=8)
listbox.pack(pady=10)

# ---------------- COUNTER ---------------- #
completed_count = 0

def mark_completed():
    global completed_count
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        completed_count += 1
        counter_label.config(text=f"Completed Tasks: {completed_count}")
        progress["value"] = completed_count * 10

tk.Button(root,
          text="Mark as Completed",
          command=mark_completed,
          bg="green", fg="white").pack(pady=5)

counter_label = tk.Label(root,
                         text="Completed Tasks: 0",
                         font=("Arial", 12),
                         bg="white")
counter_label.pack(pady=5)

# ---------------- PROGRESS BAR ---------------- #
progress = ttk.Progressbar(root,
                           orient="horizontal",
                           length=300,
                           mode="determinate")
progress.pack(pady=10)

# ---------------- DARK MODE ---------------- #
is_dark = False

def toggle_mode():
    global is_dark
    if not is_dark:
        root.configure(bg="#1e1e2f")
        header.configure(bg="#0c2461")
        task_frame.configure(bg="#1e1e2f")
        counter_label.configure(bg="#1e1e2f", fg="white")
        is_dark = True
    else:
        root.configure(bg="white")
        header.configure(bg="#2ecc71")
        task_frame.configure(bg="white")
        counter_label.configure(bg="white", fg="black")
        is_dark = False

tk.Button(root,
          text="Toggle Dark Mode",
          command=toggle_mode).pack(pady=10)

root.mainloop()
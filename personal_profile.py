import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Personal Profile Dashboard")
root.geometry("800x500")
root.configure(bg="white")

# ---------------- HEADER ---------------- #
header = tk.Label(root, text="👤 Personal Profile Dashboard",
                  font=("Arial", 18, "bold"),
                  bg="#4a69bd", fg="white",
                  height=2)
header.pack(fill=tk.X)

# ---------------- PROFILE FRAME ---------------- #
profile_frame = tk.Frame(root, bg="white")
profile_frame.pack(pady=20)

# Profile Image Placeholder
photo = tk.Label(profile_frame, text="Profile Photo",
                 width=15, height=7,
                 bg="gray", fg="white")
photo.grid(row=0, column=0, rowspan=4, padx=20)

# Profile Details
tk.Label(profile_frame, text="Name:", font=("Arial", 12), bg="white").grid(row=0, column=1, sticky="w")
name_var = tk.StringVar(value="Spoorthi S G")
name_entry = tk.Entry(profile_frame, textvariable=name_var)
name_entry.grid(row=0, column=2)

tk.Label(profile_frame, text="Email:", font=("Arial", 12), bg="white").grid(row=1, column=1, sticky="w")
email_var = tk.StringVar(value="spoorthi@example.com")
email_entry = tk.Entry(profile_frame, textvariable=email_var)
email_entry.grid(row=1, column=2)

tk.Label(profile_frame, text="Role:", font=("Arial", 12), bg="white").grid(row=2, column=1, sticky="w")
role_var = tk.StringVar(value="AI/ML Intern")
role_entry = tk.Entry(profile_frame, textvariable=role_var)
role_entry.grid(row=2, column=2)

# ---------------- SKILLS SECTION ---------------- #
tk.Label(root, text="Skills",
         font=("Arial", 14, "bold"),
         bg="white").pack(pady=10)

skills_frame = tk.Frame(root, bg="white")
skills_frame.pack()

skills = ["Python", "Machine Learning", "SQL", "Tkinter", "YOLO"]
for skill in skills:
    tk.Label(skills_frame, text=skill,
             bg="#dff9fb", width=20).pack(pady=3)

# ---------------- DARK MODE ---------------- #
is_dark = False

def toggle_mode():
    global is_dark
    if not is_dark:
        root.configure(bg="#1e1e2f")
        profile_frame.configure(bg="#1e1e2f")
        skills_frame.configure(bg="#1e1e2f")
        header.configure(bg="#0c2461")
        is_dark = True
    else:
        root.configure(bg="white")
        profile_frame.configure(bg="white")
        skills_frame.configure(bg="white")
        header.configure(bg="#4a69bd")
        is_dark = False

tk.Button(root, text="Toggle Dark Mode",
          command=toggle_mode).pack(pady=10)

# ---------------- STATUS BAR ---------------- #
status = tk.Label(root, text="Profile Loaded Successfully",
                  bd=1, relief=tk.SUNKEN,
                  anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
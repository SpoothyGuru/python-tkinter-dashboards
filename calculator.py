import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()
    
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2
    
    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")
tk.Label(root, text="Number 1:", font=("Arial", 12)).pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 12))

entry1.pack(pady=5)
tk.Label(root, text="Number 2:", font=("Arial", 12)).pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack(pady=5)
operation_var = tk.StringVar(value="Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
for op in operations:
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).pack(anchor=tk.W)

tk.Button(root, text="Calculate", command=calculate, bg="blue", fg="white", font=("Arial", 12)).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=10)
root.mainloop()
# Simple Calculator
import tkinter as tk
from tkinter import messagebox


def press(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def negative():
    text = display.get()

    if text.startswith("-"):
        display.delete(0)
    else:
        display.insert(0, "-")


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display.insert(0, str(result))

    except:
        messagebox.showerror("Error", "Invalid expression")


root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

# Large Display
display = tk.Entry(root, font=("Arial", 20), justify="right", bd=5)
display.pack(fill="x", padx=10, pady=10, ipady=10)

main_frame = tk.Frame(root)
main_frame.pack(pady=5)

# Left Side
left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", padx=5)

# Operators row
op_frame = tk.Frame(left_frame)
op_frame.pack()

for op in ["+", "-", "*", "/"]:
    tk.Button(op_frame, text=op, width=5, height=2, font=("Arial", 12),
              command=lambda o=op: press(o)).pack(side="left", padx=2)

# Utility buttons under operators
util_frame = tk.Frame(left_frame)
util_frame.pack(pady=5)

tk.Button(util_frame, text="+/-", width=10, height=2,
          command=negative).pack(side="left", padx=2)
tk.Button(util_frame, text=".", width=10, height=2,
          command=lambda: press(".")).pack(side="left", padx=2)


# Number Pad
num_frame = tk.Frame(left_frame)
num_frame.pack(pady=10)

numbers = [["7", "8", "9"],
           ["4", "5", "6"],
           ["1", "2", "3"]]


for r, row in enumerate(numbers):
    for c, num in enumerate(row):
        tk.Button(num_frame, text=num, width=6, height=2, font=("Arial", 12),
                  command=lambda n=num: press(n)).grid(row=r, column=c, padx=2, pady=2)

tk.Button(num_frame, text="0", width=6, height=2, font=("Arial", 12),
          command=lambda: press("0")).grid(row=3, column=1, padx=2, pady=2)

# Bottom row (=, Clear)
bottom_frame = tk.Frame(left_frame)
bottom_frame.pack(pady=5)

tk.Button(bottom_frame, text="=", width=6, height=2, font=("Arial", 12, "bold"), fg="blue",
          command=calculate).pack(side="left", padx=2)

tk.Button(bottom_frame, text="Clear", width=10, height=2, fg="red",
          highlightbackground="red", highlightthickness=2,
          command=clear).pack(side="left", padx=2)


root.mainloop()

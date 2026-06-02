# Simple Text Editor

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


# File operations logic
def open_file():
    # Open file dialog to choose a .txt file
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"),
                                                     ("All Files", "*.*")])
    if not filepath:
        return

    # Clear current content and insert new file content
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    # Open save file dialog with default .txt extension
    filepath = filedialog.asksaveasfilename(defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return

    # Write text component data into the selected file destination
    with open(filepath, "w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)

    window.title(f"Simple Text Editor - {filepath}")


txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

# Connected buttons to functions via the command parameter
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, padx=5, pady=5)
btn_save.grid(row=1, column=0, padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

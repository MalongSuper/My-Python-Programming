# Simple Student Table

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Table")
root.geometry("600x550")


# Function to validate and add data to the Treeview
def add_student():
    student_id = ent_id.get().strip()
    name = ent_name.get().strip()
    major = ent_major.get().strip()

    # Validation: Ensure fields are not empty
    if not student_id or not name or not major:
        messagebox.showwarning("Input Error", "All fields must be filled out!")
        return

    # Insert values into the table
    table.insert("", tk.END, values=(student_id, name, major))

    # Clear fields for the next input
    ent_id.delete(0, tk.END)
    ent_name.delete(0, tk.END)
    ent_major.delete(0, tk.END)
    ent_id.focus()


# --- Form Layout Panel (Inputs using pack) ---
frm_form = tk.LabelFrame(root, text=" Add New Student ", padx=10, pady=10)
frm_form.pack(fill="x", padx=10, pady=10)

# Student ID Row (Side-by-side inside an independent frame)
row_id = tk.Frame(frm_form)
row_id.pack(fill="x", pady=2)
lbl_id = tk.Label(row_id, text="Student ID:", width=12, anchor="w")
lbl_id.pack(side="left")
ent_id = tk.Entry(row_id)
ent_id.pack(side="left", fill="x", expand=True)

# Name Row
row_name = tk.Frame(frm_form)
row_name.pack(fill="x", pady=2)
lbl_name = tk.Label(row_name, text="Name:", width=12, anchor="w")
lbl_name.pack(side="left")
ent_name = tk.Entry(row_name)
ent_name.pack(side="left", fill="x", expand=True)

# Major Row
row_major = tk.Frame(frm_form)
row_major.pack(fill="x", pady=2)
lbl_major = tk.Label(row_major, text="Major:", width=12, anchor="w")
lbl_major.pack(side="left")
ent_major = tk.Entry(row_major)
ent_major.pack(side="left", fill="x", expand=True)

# Action Button
btn_add = tk.Button(frm_form, text="Add", command=add_student, bg="#4CAF50", fg="blue")
btn_add.pack(fill="x", pady=10)

# --- Table Layout Panel (using pack) ---
table = ttk.Treeview(root, columns=("ID", "Name", "Major"), show="headings")

table.heading("ID", text="Student ID")
table.heading("Name", text="Name")
table.heading("Major", text="Major")

# Pre-populated Data
table.insert("", tk.END, values=("101", "Alice", "Computer Science"))
table.insert("", tk.END, values=("102", "Bob", "Cybersecurity"))
table.insert("", tk.END, values=("103", "Charlie", "Business"))

table.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()

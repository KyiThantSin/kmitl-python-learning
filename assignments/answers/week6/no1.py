import tkinter as tk
from tkinter import messagebox

def append_to_display(character):
    current_text = display_var.get()
    display_var.set(current_text + character)

def delete_last_character():
    current_text = display_var.get()
    display_var.set(current_text[:-1])

def dial_number():
    current_number = display_var.get()
    messagebox.showinfo("Dialing", f"Dialing <<{current_number}>>")

root = tk.Tk()
root.title("KMITL Phone")

display_var = tk.StringVar()
display_entry = tk.Entry(root, textvariable=display_var, font=("Arial", 20), justify='right', bd=10)
display_entry.grid(row=0, column=0, columnspan=3)

button_labels = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '*', '0', '#'
]

row_index = 1
col_index = 0

for label in button_labels:
    action = lambda x=label: append_to_display(x)
    tk.Button(root, text=label, width=5, height=2, command=action).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 2:
        col_index = 0
        row_index += 1

tk.Button(root, text="Talk", width=5, height=2, command=dial_number).grid(row=row_index, column=0)
tk.Button(root, text="<", width=5, height=2, command=delete_last_character).grid(row=row_index, column=2)

root.mainloop()

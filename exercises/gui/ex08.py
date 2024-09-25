import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import ZODB, ZODB.FileStorage
import persistent
import transaction

# ZODB setup
storage = ZODB.FileStorage.FileStorage('tasks.fs')
db = ZODB.DB(storage)
connection = db.open()
root_db = connection.root()

# Initialize task list if it doesn't exist
if not hasattr(root_db, 'tasks'):
    root_db.tasks = []

# Initialize customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Task class for ZODB
class Task(persistent.Persistent):
    def __init__(self, name, description, tag, status, date):
        self.name = name
        self.description = description
        self.tag = tag
        self.status = status
        self.date = date

class TaskManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management System")
        self.root.geometry("800x600")
        
        # Task form variables
        self.task_name_var = ctk.StringVar()
        self.description_var = ctk.StringVar()
        self.tag_var = ctk.StringVar()
        self.status_var = ctk.StringVar()
        self.date_var = ctk.StringVar()

        # Filter variables
        self.filter_tag_var = ctk.StringVar()
        self.filter_status_var = ctk.StringVar()

        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        # Task form
        form_frame = ctk.CTkFrame(self.root, corner_radius=10)
        form_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(form_frame, text="Task Name:").grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkEntry(form_frame, textvariable=self.task_name_var).grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Description:").grid(row=1, column=0, padx=10, pady=5)
        ctk.CTkEntry(form_frame, textvariable=self.description_var).grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Tag:").grid(row=2, column=0, padx=10, pady=5)
        self.tag_combobox = ctk.CTkComboBox(form_frame, values=["Work", "Personal", "Urgent"], variable=self.tag_var)
        self.tag_combobox.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Status:").grid(row=3, column=0, padx=10, pady=5)
        self.status_combobox = ctk.CTkComboBox(form_frame, values=["Pending", "In Progress", "Completed"], variable=self.status_var)
        self.status_combobox.grid(row=3, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Date (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
        ctk.CTkEntry(form_frame, textvariable=self.date_var).grid(row=4, column=1, padx=10, pady=5)

        ctk.CTkButton(form_frame, text="Add Task", command=self.add_task).grid(row=5, columnspan=2, pady=10)

        # Task filter
        filter_frame = ctk.CTkFrame(self.root, corner_radius=10)
        filter_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(filter_frame, text="Filter by Tag:").grid(row=0, column=0, padx=10, pady=5)
        self.filter_tag_combobox = ctk.CTkComboBox(filter_frame, values=["", "Work", "Personal", "Urgent"], variable=self.filter_tag_var)
        self.filter_tag_combobox.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(filter_frame, text="Filter by Status:").grid(row=0, column=2, padx=10, pady=5)
        self.filter_status_combobox = ctk.CTkComboBox(filter_frame, values=["", "Pending", "In Progress", "Completed"], variable=self.filter_status_var)
        self.filter_status_combobox.grid(row=0, column=3, padx=10, pady=5)

        ctk.CTkButton(filter_frame, text="Apply Filter", command=self.filter_tasks).grid(row=0, column=4, padx=10)
        ctk.CTkButton(filter_frame, text="Clear Filter", command=self.clear_filter).grid(row=0, column=5, padx=10)

        # Task list
        self.task_list_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.task_list_frame.pack(pady=10, padx=20, fill="both", expand=True)

    def load_tasks(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
        
        for task in root_db.tasks:
            self.create_task_card(task)

    def create_task_card(self, task):
        card_frame = ctk.CTkFrame(self.task_list_frame, corner_radius=10)
        card_frame.pack(fill="x", pady=5, padx=10)

        ctk.CTkLabel(card_frame, text=f"Task: {task.name}", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="w", padx=10)
        ctk.CTkLabel(card_frame, text=f"Description: {task.description}").grid(row=1, column=0, sticky="w", padx=10)
        ctk.CTkLabel(card_frame, text=f"Tag: {task.tag}").grid(row=2, column=0, sticky="w", padx=10)
        ctk.CTkLabel(card_frame, text=f"Status: {task.status}").grid(row=3, column=0, sticky="w", padx=10)
        ctk.CTkLabel(card_frame, text=f"Date: {task.date}").grid(row=4, column=0, sticky="w", padx=10)

        edit_button = ctk.CTkButton(card_frame, text="Edit", command=lambda t=task: self.edit_task(t))
        edit_button.grid(row=5, column=0, padx=10, pady=(5, 0), sticky="e")

        delete_button = ctk.CTkButton(card_frame, text="Delete", command=lambda t=task: self.delete_task(t))
        delete_button.grid(row=5, column=1, padx=10, pady=(5, 0), sticky="e")

    def add_task(self):
        task_name = self.task_name_var.get()
        description = self.description_var.get()
        tag = self.tag_var.get()
        status = self.status_var.get()
        date = self.date_var.get()

        if not task_name or not date:
            messagebox.showerror("Error", "Task name and date are required!")
            return
        
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Date format should be YYYY-MM-DD.")
            return

        new_task = Task(task_name, description, tag, status, date)
        root_db.tasks.append(new_task)
        transaction.commit()  # Save changes to ZODB
        
        self.clear_form()
        self.load_tasks()

    def clear_form(self):
        self.task_name_var.set("")
        self.description_var.set("")
        self.tag_var.set("")
        self.status_var.set("")
        self.date_var.set("")

    def delete_task(self, task):
        root_db.tasks.remove(task)
        transaction.commit()
        self.load_tasks()

    def edit_task(self, task):
        self.task_name_var.set(task.name)
        self.description_var.set(task.description)
        self.tag_var.set(task.tag)
        self.status_var.set(task.status)
        self.date_var.set(task.date)

        save_button = ctk.CTkButton(self.root, text="Save Changes", command=lambda: self.save_task(task))
        save_button.pack(pady=5)

    def save_task(self, task):
        task.name = self.task_name_var.get()
        task.description = self.description_var.get()
        task.tag = self.tag_var.get()
        task.status = self.status_var.get()
        task.date = self.date_var.get()

        try:
            datetime.strptime(task.date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Date format should be YYYY-MM-DD.")
            return

        transaction.commit()
        self.clear_form()
        self.load_tasks()

    def filter_tasks(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        tag_filter = self.filter_tag_var.get()
        status_filter = self.filter_status_var.get()

        filtered_tasks = [
            task for task in root_db.tasks 
            if (not tag_filter or task.tag == tag_filter) and (not status_filter or task.status == status_filter)
        ]

        for task in filtered_tasks:
            self.create_task_card(task)

    def clear_filter(self):
        self.filter_tag_var.set("")
        self.filter_status_var.set("")
        self.load_tasks()

if __name__ == "__main__":
    root = ctk.CTk()
    task_manager = TaskManagementSystem(root)
    root.mainloop()

    # Close ZODB connection when the app closes
    connection.close()
    db.close()

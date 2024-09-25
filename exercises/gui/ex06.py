import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import sqlite3

# Database setup
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
              (id INTEGER PRIMARY KEY, name TEXT, description TEXT, tag TEXT, status TEXT, date TEXT)''')
conn.commit()

class TaskManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management System")
        self.root.geometry("700x500")
        self.tasks = []
        
        # Task form variables
        self.task_name_var = tk.StringVar()
        self.description_var = tk.StringVar()
        self.tag_var = tk.StringVar()
        self.status_var = tk.StringVar()
        self.date_var = tk.StringVar()
        
        # Filter variables
        self.filter_tag_var = tk.StringVar()
        self.filter_status_var = tk.StringVar()
        
        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        # Task form
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="Task Name:").grid(row=0, column=0)
        tk.Entry(form_frame, textvariable=self.task_name_var).grid(row=0, column=1)
        
        tk.Label(form_frame, text="Description:").grid(row=1, column=0)
        tk.Entry(form_frame, textvariable=self.description_var).grid(row=1, column=1)
        
        tk.Label(form_frame, text="Tag:").grid(row=2, column=0)
        self.tag_combobox = ttk.Combobox(form_frame, textvariable=self.tag_var, values=["Work", "Personal", "Urgent"], state="readonly")
        self.tag_combobox.grid(row=2, column=1)
        
        tk.Label(form_frame, text="Status:").grid(row=3, column=0)
        self.status_combobox = ttk.Combobox(form_frame, textvariable=self.status_var, values=["Pending", "In Progress", "Completed"], state="readonly")
        self.status_combobox.grid(row=3, column=1)
        
        tk.Label(form_frame, text="Date (YYYY-MM-DD):").grid(row=4, column=0)
        tk.Entry(form_frame, textvariable=self.date_var).grid(row=4, column=1)
        
        tk.Button(form_frame, text="Add Task", command=self.add_task).grid(row=5, columnspan=2, pady=10)
        
        # Task filter
        filter_frame = tk.Frame(self.root)
        filter_frame.pack(pady=10)
        
        tk.Label(filter_frame, text="Filter by Tag:").grid(row=0, column=0)
        self.filter_tag_combobox = ttk.Combobox(filter_frame, textvariable=self.filter_tag_var, values=["", "Work", "Personal", "Urgent"], state="readonly")
        self.filter_tag_combobox.grid(row=0, column=1)
        
        tk.Label(filter_frame, text="Filter by Status:").grid(row=0, column=2)
        self.filter_status_combobox = ttk.Combobox(filter_frame, textvariable=self.filter_status_var, values=["", "Pending", "In Progress", "Completed"], state="readonly")
        self.filter_status_combobox.grid(row=0, column=3)
        
        tk.Button(filter_frame, text="Apply Filter", command=self.filter_tasks).grid(row=0, column=4, padx=5)
        tk.Button(filter_frame, text="Clear Filter", command=self.clear_filter).grid(row=0, column=5)
        
        # Task list
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(pady=10)
    
    def load_tasks(self):
        # Clear current task cards
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
        
        # Fetch tasks from database
        cursor.execute("SELECT * FROM tasks")
        self.tasks = cursor.fetchall()
        
        # Display tasks as cards
        for task in self.tasks:
            self.create_task_card(task)

    def create_task_card(self, task):
        card_frame = tk.Frame(self.task_list_frame, bd=2, relief="groove", padx=10, pady=5)
        card_frame.pack(fill="x", pady=5)
        
        tk.Label(card_frame, text=f"Task: {task[1]}", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="w")
        tk.Label(card_frame, text=f"Description: {task[2]}").grid(row=1, column=0, sticky="w")
        tk.Label(card_frame, text=f"Tag: {task[3]}").grid(row=2, column=0, sticky="w")
        tk.Label(card_frame, text=f"Status: {task[4]}").grid(row=3, column=0, sticky="w")
        tk.Label(card_frame, text=f"Date: {task[5]}").grid(row=4, column=0, sticky="w")
        
        edit_button = tk.Button(card_frame, text="Edit", command=lambda t=task: self.edit_task(t))
        edit_button.grid(row=0, column=1, padx=10)
        
        delete_button = tk.Button(card_frame, text="Delete", command=lambda t=task: self.delete_task(t[0]))
        delete_button.grid(row=0, column=2, padx=10)

    def add_task(self):
        # Get task data
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
            messagebox.showerror("Error", "Invalid date format!")
            return
        
        # Add task to database
        cursor.execute("INSERT INTO tasks (name, description, tag, status, date) VALUES (?, ?, ?, ?, ?)", 
                       (task_name, description, tag, status, date))
        conn.commit()
        
        self.clear_form()
        self.load_tasks()
    
    def clear_form(self):
        self.task_name_var.set("")
        self.description_var.set("")
        self.tag_var.set("")
        self.status_var.set("")
        self.date_var.set("")
    
    def delete_task(self, task_id):
        # Delete task from database
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        self.load_tasks()
    
    def edit_task(self, task):
        self.task_name_var.set(task[1])
        self.description_var.set(task[2])
        self.tag_var.set(task[3])
        self.status_var.set(task[4])
        self.date_var.set(task[5])
        
        # Add a Save button for editing
        save_button = tk.Button(self.root, text="Save Changes", command=lambda: self.save_task(task[0]))
        save_button.pack(pady=5)
    
    def save_task(self, task_id):
        task_name = self.task_name_var.get()
        description = self.description_var.get()
        tag = self.tag_var.get()
        status = self.status_var.get()
        date = self.date_var.get()
        
        cursor.execute("UPDATE tasks SET name=?, description=?, tag=?, status=?, date=? WHERE id=?",
                       (task_name, description, tag, status, date, task_id))
        conn.commit()
        self.clear_form()
        self.load_tasks()
    
    def filter_tasks(self):
        # Clear current task cards
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
        
        tag_filter = self.filter_tag_var.get()
        status_filter = self.filter_status_var.get()
        
        query = "SELECT * FROM tasks WHERE 1=1"
        params = []
        
        if tag_filter:
            query += " AND tag = ?"
            params.append(tag_filter)
        if status_filter:
            query += " AND status = ?"
            params.append(status_filter)
        
        cursor.execute(query, params)
        filtered_tasks = cursor.fetchall()
        
        for task in filtered_tasks:
            self.create_task_card(task)
    
    def clear_filter(self):
        self.filter_tag_var.set("")
        self.filter_status_var.set("")
        self.load_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagementSystem(root)
    root.mainloop()

# Close the database connection when done
conn.close()

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('newtesting.db')

# Create a cursor
cursor = conn.cursor()

# Create a tasks table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        status TEXT
    )
''')

def insert_task(title, due_date):
    try:
        # Execute the INSERT statement with due_date
        cursor.execute("INSERT INTO tasks (title, due_date) VALUES (?, ?)", (title, due_date))
        
        # Commit the changes
        conn.commit()
        print(f"Inserted task: {title} with due date: {due_date}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Insert some sample tasks with due dates
insert_task('Learn SQLite', '2024-10-01')
insert_task('Build a Python project', '2024-10-15')

# Commit the changes
conn.commit()

# Function to filter tasks by due date
def filter_tasks_by_due_date(date):
    cursor.execute("SELECT * FROM tasks WHERE due_date = ?", (date,))
    return cursor.fetchall()

# Example usage of filtering
filtered_tasks = filter_tasks_by_due_date('2024-10-01')
print("Filtered Tasks:")
for task in filtered_tasks:
    print(task)

# Verify the table was created
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# Close the connection
conn.close()

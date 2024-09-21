import sqlite3

# Connect to the database
conn = sqlite3.connect('/Users/kyithantsin/testing.db')

# Create a cursor object
cursor = conn.cursor()

# Define a function to insert data into the tasks table
def insert_task(title):
    try:
        # Execute the INSERT statement
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        
        # Commit the changes
        conn.commit()
        print(f"Inserted task: {title}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Insert some sample tasks
insert_task('Learn SQLite')
insert_task('Build a Python project')

# Close the connection
conn.close()

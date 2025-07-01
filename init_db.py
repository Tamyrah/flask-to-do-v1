import sqlite3

# Connect to (or create) the todo.db database
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Open and read the SQL schema file
with open('schema.sql', 'r') as f:
    sql = f.read()

# Execute the schema SQL to create the tasks table
cursor.executescript(sql)

# Save changes and close the connection
conn.commit()
conn.close()

print("Database created successfully.")

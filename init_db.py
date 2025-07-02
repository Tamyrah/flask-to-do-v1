import sqlite3

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

with open('schema.sql', 'r') as f:
    sql = f.read()

cursor.executescript(sql)
conn.commit()
conn.close()

print("Database created successfully.")

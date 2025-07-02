import sqlite3

def init_db():
    conn = sqlite3.connect('todo.db')
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()



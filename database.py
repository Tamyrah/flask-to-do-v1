import sqlite3
import os

DB_FILE = os.path.join(os.path.dirname(__file__), 'instance', 'todo.db')
SCHEMA_FILE = os.path.join(os.path.dirname(__file__), 'schema.sql')

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        with open(SCHEMA_FILE, "r") as f:
            conn.executescript(f.read())



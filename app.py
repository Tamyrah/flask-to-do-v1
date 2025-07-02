from flask import Flask, render_template, request, redirect
import sqlite3
import os
from database import init_db

app = Flask(__name__)

# Define path to the database in the instance folder
DB_FILE = os.path.join(os.path.dirname(__file__), 'instance', 'todo.db')

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    if request.method == "POST":
        content = request.form["content"]
        due_date = request.form.get("due_date")
        priority = request.form.get("priority")
        conn.execute("INSERT INTO tasks (content, due_date, priority) VALUES (?, ?, ?)",


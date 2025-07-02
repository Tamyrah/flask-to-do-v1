from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (task, completed) VALUES (?, ?)', (task, 0))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete(task_id):
    conn = get_db_connection()
conn.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))





































from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home page – show all tasks
@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Add new task
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (task, completed) VALUES (?, ?)', (task, False))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Mark task as complete
@app.route('/complete/<int:task_id>')
def complete(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Delete a task
@app.route('/delete/<int:task_id>')
def delete(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



































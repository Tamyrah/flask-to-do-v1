from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_FILE = 'instance/todo.db'


def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()

    if request.method == 'POST':
        content = request.form['content']
        due_date = request.form.get('due_date')  # Optional field
        priority = request.form.get('priority')  # Optional field

        conn.execute(
            'INSERT INTO tasks (content, due_date, priority) VALUES (?, ?, ?)',
            (content, due_date, priority)
        )
        conn.commit()
        conn.close()
        return redirect('/')

    tasks = conn.execute('SELECT * FROM tasks ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)


@app.route('/complete/<int:task_id>')
def complete(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)


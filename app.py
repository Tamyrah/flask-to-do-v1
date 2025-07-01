from flask import Flask, render_template, request, redirect
from database import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/', methods=['POST'])
def add():
    task_content = request.form['content']
    due_date = request.form['due_date']
    priority = request.form['priority']
    
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO tasks (content, due_date, priority) VALUES (?, ?, ?)',
        (task_content, due_date, priority)
    )
    conn.commit()
    conn.close()
    return redirect('/')

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































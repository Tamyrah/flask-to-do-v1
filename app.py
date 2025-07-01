from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for form handling (can be anything random)

# ---------- Database Connection Helper ----------
def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn

# ---------- Home Route (GET + POST) ----------
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()

    if request.method == 'POST':
        task = request.form['task']
        if task:
            conn.execute('INSERT INTO tasks (task, completed) VALUES (?, ?)', (task, 0))
            conn.commit()
        conn.close()
        return redirect('/')

    # GET request: show tasks
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# ---------- Complete Task ----------
@app.route('/complete/<int:task_id>')
def complete(task_id):


































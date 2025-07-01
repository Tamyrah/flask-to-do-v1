@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    if request.method == 'POST':
        task = request.form['task']
        due_date = request.form['due_date']
        priority = request.form['priority']
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn.execute(
            'INSERT INTO tasks (task, due_date, priority, created_at) VALUES (?, ?, ?, ?)',
            (task, due_date, priority, created_at)
        )
        conn.commit()
    tasks = conn.execute('SELECT * FROM tasks ORDER BY completed, priority DESC, due_date').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)


































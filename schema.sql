DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0,
    due_date TEXT,
    priority TEXT,
    status TEXT DEFAULT 'Want to Read',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);






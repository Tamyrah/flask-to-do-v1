<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask To-Do App</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
<div class="container py-5">
    <h2 class="mb-4">My To-Do List</h2>
    <form method="POST" action="/">
        <div class="form-group d-flex">
            <input type="text" name="task" class="form-control mr-2" placeholder="Enter a new task">
            <button type="submit" class="btn btn-primary">Add Task</button>
        </div>
    </form>

    <ul class="list-group mt-4">
        {% for task in tasks %}
        <li class="list-group-item d-flex justify-content-between align-items-center {% if task['completed'] %}list-group-item-success{% endif %}">
            {{ task['task'] }}
            <div>
                {% if not task['completed'] %}
                <a href="/complete/{{ task['id'] }}" class="btn btn-success btn-sm mr-2">Complete</a>
                {% endif %}
                <a href="/delete/{{ task['id'] }}" class="btn btn-danger btn-sm">Delete</a>
            </div>
        </li>
        {% endfor %}
    </ul>
</div>
</body>
</html>



































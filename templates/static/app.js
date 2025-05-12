document.getElementById("task-form").addEventListener("submit", async function(event) {
  event.preventDefault();

  const taskInput = document.getElementById("task-input");
  const taskText = taskInput.value.trim();

  if (taskText) {
    const response = await fetch('/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: taskText })
    });

    const newTask = await response.json();

    const taskList = document.getElementById("task-list");
    const li = document.createElement("li");
    li.textContent = newTask.title;
    taskList.appendChild(li);

    taskInput.value = "";
  }
});

window.addEventListener("DOMContentLoaded", async () => {
  const response = await fetch('/tasks');
  const tasks = await response.json();

  const taskList = document.getElementById("task-list");
  tasks.forEach(task => {
    const li = document.createElement("li");
    li.textContent = task.title;
    taskList.appendChild(li);
  });
});







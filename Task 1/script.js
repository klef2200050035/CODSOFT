document.addEventListener('DOMContentLoaded', function () {
    const taskForm = document.getElementById('task-form');
    const taskList = document.getElementById('task-list');
    
    // Load tasks from local storage
    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    // Render tasks on load
    renderTasks();

    taskForm.addEventListener('submit', function (e) {
        e.preventDefault();
        
        const taskTitle = document.getElementById('task-title').value;
        const taskDesc = document.getElementById('task-desc').value;
        const taskDueDate = document.getElementById('task-due-date').value;
        const taskPriority = document.getElementById('task-priority').value;

        const newTask = {
            id: Date.now(),
            title: taskTitle,
            desc: taskDesc,
            dueDate: taskDueDate,
            priority: taskPriority,
            completed: false
        };

        tasks.push(newTask);
        saveTasks();
        renderTasks();
        taskForm.reset();
    });

    function renderTasks() {
        taskList.innerHTML = '';

        tasks.forEach(task => {
            const li = document.createElement('li');
            li.className = task.completed ? 'completed' : '';
            
            li.innerHTML = `
                <div class="task-details">
                    <div class="task-title">${task.title}</div>
                    <div class="task-desc">${task.desc}</div>
                    <div class="task-due-date">Due: ${task.dueDate}</div>
                    <div class="task-priority">Priority: ${task.priority}</div>
                </div>
                <div class="task-actions">
                    <button class="complete-button">${task.completed ? 'Undo' : 'Complete'}</button>
                    <button class="edit-button">Edit</button>
                    <button class="delete-button">Delete</button>
                </div>
            `;

            taskList.appendChild(li);

            const completeButton = li.querySelector('.complete-button');
            const editButton = li.querySelector('.edit-button');
            const deleteButton = li.querySelector('.delete-button');

            completeButton.addEventListener('click', () => toggleComplete(task.id));
            editButton.addEventListener('click', () => editTask(task.id));
            deleteButton.addEventListener('click', () => deleteTask(task.id));
        });
    }

    function toggleComplete(taskId) {
        tasks = tasks.map(task => task.id === taskId ? { ...task, completed: !task.completed } : task);
        saveTasks();
        renderTasks();
    }

    function editTask(taskId) {
        const task = tasks.find(task => task.id === taskId);
        document.getElementById('task-title').value = task.title;
        document.getElementById('task-desc').value = task.desc;
        document.getElementById('task-due-date').value = task.dueDate;
        document.getElementById('task-priority').value = task.priority;

        deleteTask(taskId);
    }

    function deleteTask(taskId) {
        tasks = tasks.filter(task => task.id !== taskId);
        saveTasks();
        renderTasks();
    }

    function saveTasks() {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }
});

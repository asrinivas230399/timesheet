document.addEventListener('DOMContentLoaded', function() {
    const projectList = document.querySelector('.project-list');

    fetch_project_data();

    function fetch_project_data() {
        fetch('/api/projects')
            .then(response => response.json())
            .then(data => {
                data.forEach(project => {
                    const projectItem = document.createElement('div');
                    projectItem.className = 'project-item';
                    projectItem.innerHTML = `
                        <h2>${project.name}</h2>
                        <p>${project.description}</p>
                        <div class="task-indicators"></div>
                    `;
                    projectList.appendChild(projectItem);
                    display_task_indicators(projectItem, project.tasks);
                });
            })
            .catch(error => console.error('Error fetching project data:', error));
    }

    function apply_filters(criteria) {
        fetch('/api/projects')
            .then(response => response.json())
            .then(data => {
                const filteredData = data.filter(project => {
                    // Apply filtering logic based on criteria
                    // Example: return project.category === criteria.category;
                    return true; // Placeholder for actual filtering logic
                });

                // Clear existing projects
                projectList.innerHTML = '';

                // Render filtered projects
                filteredData.forEach(project => {
                    const projectItem = document.createElement('div');
                    projectItem.className = 'project-item';
                    projectItem.innerHTML = `
                        <h2>${project.name}</h2>
                        <p>${project.description}</p>
                        <div class="task-indicators"></div>
                    `;
                    projectList.appendChild(projectItem);
                    display_task_indicators(projectItem, project.tasks);
                });
            })
            .catch(error => console.error('Error applying filters:', error));
    }

    function display_task_indicators(projectItem, tasks) {
        const taskIndicators = projectItem.querySelector('.task-indicators');
        tasks.forEach(task => {
            const indicator = document.createElement('span');
            indicator.className = 'task-indicator';
            indicator.style.backgroundColor = task.completed ? 'green' : 'red';
            taskIndicators.appendChild(indicator);
        });
    }

    // Example usage of apply_filters
    // apply_filters({ category: 'Web Development' });
});
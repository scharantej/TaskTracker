# Flask Application Design
## Overview
- The Flask application is designed to create a recurring todo tracker that informs the user of tasks requiring more focus and tasks on track.

## HTML Files
### `index.html`
- **Purpose**: This is the landing page of the application and provides the user interface for adding and viewing tasks.
- **Content**:
  - Navigation bar with links to different sections of the application, including a 'Create Task' link.
  - A form to add a new task, consisting of fields for task name, category (such as work, personal, or chores), and due date.
  - A table to display all tasks, including columns for task name, category, due date, and status (on track/needs focus).

### `task_detail.html`
- **Purpose**: Provides details about a specific task and allows the user to mark it as completed or update its status.
- **Content**:
  - Basic information about the task, including name, category, due date, and status.
  - A form to update the task details, including a field to add comments.
  - Buttons for marking the task as completed or changing its status to 'needs focus' or 'on track'.

## Routes
### `/`
- **Purpose**: Displays the landing page, `index.html`.

### `/create_task`
- **Purpose**: Processes the submitted form from `index.html` to create a new task.
- **Functionality**:
  - Extracts the task name, category, and due date from the form data.
  - Validates the data to ensure all required fields are present.
  - Creates a new task object and adds it to the database.
  - Redirects the user to the landing page, `index.html`.

### `/view_tasks`
- **Purpose**: Displays a table with all the tasks stored in the database.
- **Functionality**:
  - Fetches all tasks from the database.
  - Renders the `index.html` page with the populated tasks table.

### `/task_detail/<task_id>`
- **Purpose**: Displays the details of a specific task.
- **Functionality**:
  - Extracts the `task_id` parameter from the URL.
  - Fetches the corresponding task from the database.
  - Renders the `task_detail.html` page with the task details.

### `/update_task/<task_id>`
- **Purpose**: Processes the submitted form from `task_detail.html` to update a task.
- **Functionality**:
  - Extracts the updated task details from the form data.
  - Validates the data to ensure all required fields are present.
  - Updates the corresponding task in the database.
  - Redirects the user to the task detail page, `task_detail.html`.

### `/mark_completed/<task_id>`
- **Purpose**: Marks a task as completed.
- **Functionality**:
  - Extracts the `task_id` parameter from the URL.
  - Fetches the corresponding task from the database.
  - Updates the task status to 'Completed' in the database.
  - Redirects the user to the landing page, `index.html`.

### `/change_status/<task_id>`
- **Purpose**: Changes the status of a task to either 'needs focus' or 'on track'.
- **Functionality**:
  - Extracts the `task_id` parameter from the URL and the new status value from the request data.
  - Validates the new status value to ensure it's either 'needs focus' or 'on track'.
  - Updates the task status in the database.
  - Redirects the user to the task detail page, `task_detail.html`.

## Database
- The application will require a database to store the tasks and their details.
- The schema of the database should include tables for tasks, categories, and, possibly, users (if the application is designed to support multiple users).
- The task table should have columns for task ID, task name, category, due date, completion status, and the user ID (if applicable).
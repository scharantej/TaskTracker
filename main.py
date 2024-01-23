
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Create Flask application instance
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='On Track')

    def __repr__(self):
        return f'<Task {self.id}>'

# Create the database tables
db.create_all()

# Define routes
@app.route('/')
def index():
    """Display the landing page."""
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/create_task', methods=['POST'])
def create_task():
    """Create a new task."""
    # Extract task details from the form
    name = request.form['name']
    category = request.form['category']
    due_date = request.form['due_date']

    # Validate the data
    if not name or not category or not due_date:
        flash('Please fill in all fields.', 'error')
        return redirect(url_for('index'))

    # Create a new task object
    task = Task(name=name, category=category, due_date=due_date)

    # Add the task to the database
    db.session.add(task)
    db.session.commit()

    # Redirect to the landing page
    flash('Task created successfully.', 'success')
    return redirect(url_for('index'))


@app.route('/view_tasks')
def view_tasks():
    """Display all tasks."""
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/task_detail/<int:task_id>')
def task_detail(task_id):
    """Display the details of a specific task."""
    task = Task.query.get_or_404(task_id)
    return render_template('task_detail.html', task=task)


@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    """Update a task."""
    # Extract updated task details from the form
    name = request.form['name']
    category = request.form['category']
    due_date = request.form['due_date']
    status = request.form['status']

    # Validate the data
    if not name or not category or not due_date:
        flash('Please fill in all fields.', 'error')
        return redirect(url_for('task_detail', task_id=task_id))

    # Fetch the task from the database
    task = Task.query.get_or_404(task_id)

    # Update the task details
    task.name = name
    task.category = category
    task.due_date = due_date
    task.status = status

    # Commit the changes to the database
    db.session.commit()

    # Redirect to the task detail page
    flash('Task updated successfully.', 'success')
    return redirect(url_for('task_detail', task_id=task_id))


@app.route('/mark_completed/<int:task_id>')
def mark_completed(task_id):
    """Mark a task as completed."""
    # Fetch the task from the database
    task = Task.query.get_or_404(task_id)

    # Set the task status to 'Completed'
    task.status = 'Completed'

    # Commit the changes to the database
    db.session.commit()

    # Redirect to the landing page
    flash('Task marked as completed.', 'success')
    return redirect(url_for('index'))


@app.route('/change_status/<int:task_id>')
def change_status(task_id):
    """Change the status of a task."""
    # Fetch the task from the database
    task = Task.query.get_or_404(task_id)

    # Get the new status from the request
    new_status = request.args.get('status')

    # Validate the new status
    if new_status not in ['Needs Focus', 'On Track']:
        flash('Invalid status.', 'error')
        return redirect(url_for('task_detail', task_id=task_id))

    # Update the task status
    task.status = new_status

    # Commit the changes to the database
    db.session.commit()

    # Redirect to the task detail page
    flash('Task status changed successfully.', 'success')
    return redirect(url_for('task_detail', task_id=task_id))


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

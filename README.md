# Task Manager

A simple Django-based Task Manager that allows users to add, complete, and delete tasks.

## Features
- Add new tasks
- Mark tasks as completed
- Delete tasks
- View all tasks

## Project Structure
```
task_manager/
│── task_manager/       # Project directory
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
│── tasks/              # App directory
│   ├── migrations/
│   ├── templates/tasks/
│   │   ├── index.html  # Main template
│   ├── static/tasks/
│   │   ├── styles.css  # Optional styling
│   ├── models.py       # Task model
│   ├── views.py        # Logic for tasks
│   ├── urls.py         # URL routing
│   ├── forms.py        # Django form (optional)
│   ├── admin.py        # Admin panel setup
│
│── db.sqlite3          # Database
│── manage.py           # Django command-line tool
```

## Installation & Setup

### Prerequisites
- Python 3.x
- Django

### Installation Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
   ```
2. **Create a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run migrations**
   ```sh
   python manage.py migrate
   ```
5. **Start the development server**
   ```sh
   python manage.py runserver
   ```
6. **Open in browser:**
   - Go to: `http://127.0.0.1:8000/`

## Usage
- **Add Task:** Enter a task name and click "Add Task."
- **Complete Task:** Click the checkbox to mark as complete.
- **Delete Task:** Click the delete button next to a task.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.


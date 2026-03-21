# 📋 Hangarin - Task Management System

A modern, responsive Django-based task management application with priority levels, categories, and comprehensive filtering capabilities.

## Table of Contents
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [How to Use](#how-to-use)
- [Features](#features)
- [API Documentation](#api-documentation)
- [Troubleshooting](#troubleshooting)

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (venv)

### Quick Start Script

```powershell
# Navigate to project directory
cd "c:\Users\Pits\Documents\3rd Year 2nd Sem\AppDev\hangarin\Hangarin"

# Activate virtual environment
.\Scripts\Activate.ps1

# Install dependencies (if needed)
pip install -r requirements.txt

# Initialize default data
python manage.py init_data

# Start the server
python manage.py runserver
```

Visit: http://localhost:8000/

---

## Installation

### 1. Clone or Download the Project
```bash
git clone https://github.com/YOUR_USERNAME/hangarin.git
cd hangarin/Hangarin
```

### 2. Create Virtual Environment
```powershell
python -m venv venv
```

### 3. Activate Virtual Environment
```powershell
# On Windows
.\Scripts\Activate.ps1

# On Mac/Linux
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Initialize Database
```bash
python manage.py migrate
python manage.py init_data
```

### 6. Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

---

## Running the Application

### Start Development Server
```bash
python manage.py runserver
```

Server runs at: **http://localhost:8000/**

### Access Admin Panel
```
URL: http://localhost:8000/admin/
Username & Password: Your superuser credentials
```

---

## How to Use

### 📊 Dashboard
**URL:** http://localhost:8000/ or http://localhost:8000/dashboard/

**Features:**
- View task statistics (Total, Pending, In Progress, Completed)
- See recent 5 tasks at a glance
- Quick action buttons to create or view all tasks
- Color-coded statistics display

### 📋 All Tasks
**URL:** http://localhost:8000/tasks/

**Features:**
- View all tasks in a responsive table
- Filter by:
  - **Status**: Pending, In Progress, Completed
  - **Priority**: High, Medium, Low
  - **Category**: Work, Personal, Shopping, Health, Learning, Projects, Home, Finance
- Quick action buttons (View, Edit, Delete)
- Task count display

### ✨ Create New Task
**URL:** http://localhost:8000/tasks/create/

**Fields:**
1. **Title** *(Required)* - Clear, descriptive task name
2. **Description** *(Optional)* - Detailed information
3. **Status** - Pending, In Progress, or Completed
4. **Priority** *(Optional)* - 🔴 High, 🟡 Medium, 🟢 Low
5. **Category** *(Optional)* - Assign to a category
6. **Deadline** *(Optional)* - Set a due date and time

**Steps:**
1. Fill in the title
2. (Optional) Add a description
3. Select status (defaults to Pending)
4. (Optional) Choose priority level
5. (Optional) Select a category
6. (Optional) Set a deadline
7. Click **Create Task**

### 👁️ View Task Details
**URL:** http://localhost:8000/tasks/<task_id>/

**Shows:**
- Full task information
- Status with color badge
- Priority indicator
- Category assignment
- Creation and last updated timestamps
- Deadline information
- Edit and Delete buttons

### ✏️ Edit Task
**URL:** http://localhost:8000/tasks/<task_id>/edit/

**Allows you to:**
- Update task title
- Modify description
- Change status
- Update priority
- Change category
- Adjust deadline
- View when task was created and last updated

**Steps:**
1. Navigate to task detail page
2. Click **Edit** button
3. Modify the desired fields
4. Click **Save Changes**

### 🗑️ Delete Task
**URL:** http://localhost:8000/tasks/<task_id>/delete/

**Steps:**
1. Navigate to task detail or task list
2. Click **Delete** button
3. Review task details on confirmation page
4. Click **Yes, Delete This Task** to confirm
5. You'll be redirected to task list

---

## Features

### ✅ Task Management
- **Create**: Add new tasks with detailed information
- **Read**: View all tasks or individual task details
- **Update**: Edit any task at any time
- **Delete**: Remove tasks with confirmation

### 🎯 Priorities
- **High** (🔴) - Urgent tasks
- **Medium** (🟡) - Normal priority
- **Low** (🟢) - Flexible timeline

### 📁 Categories
- Work
- Personal
- Shopping
- Health
- Learning
- Projects
- Home
- Finance

### 🔍 Filtering
- Filter by Status
- Filter by Priority
- Filter by Category
- Combine multiple filters
- Reset filters to see all tasks

### 📊 Statistics
- Total task count
- Pending tasks count
- In-progress tasks count
- Completed tasks count
- Recent tasks display

### 🎨 User Interface
- Responsive design (mobile, tablet, desktop)
- Bootstrap 5.3 styling
- Color-coded badges and indicators
- Emoji icons for visual clarity
- Smooth navigation and transitions

### 🔐 Admin Panel
- Add/edit priorities and categories
- Manage all tasks with advanced filtering
- View and manage subtasks and notes
- Bulk operations support
- Full Django admin features

---

## API Documentation

### 📡 JSON API Endpoints

#### Get All Tasks
```
GET /api/tasks/
```

**Query Parameters:**
- `status`: Filter by status (Pending, In Progress, Completed)
- `priority_id`: Filter by priority ID
- `category_id`: Filter by category ID

**Example:**
```
/api/tasks/?status=Pending&priority_id=1
```

**Response:**
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Task Title",
      "description": "Task description",
      "status": "Pending",
      "deadline": "2026-03-20T10:00:00Z",
      "priority": "High",
      "category": "Work",
      "created_at": "2026-03-15T10:00:00Z",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "count": 1
}
```

#### Get Specific Task
```
GET /api/tasks/<task_id>/
```

**Response:**
```json
{
  "task": {
    "id": 1,
    "title": "Task Title",
    ...
  }
}
```

---

## Project Structure

```
hangarin/
├── hangarin_project/       # Main Django project config
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI config
│   └── asgi.py            # ASGI config
├── tasks/                 # Task management app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # App URL routing
│   ├── admin.py           # Admin configuration
│   ├── templates/         # HTML templates
│   ├── management/        # Custom commands
│   │   └── commands/
│   │       └── init_data.py  # Data initialization
│   ├── fixtures/          # Data fixtures
│   └── migrations/        # Database migrations
├── manage.py              # Django management CLI
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

---

## Database Models

### Task
```
- title (CharField): Task name
- description (TextField): Optional details
- status (CharField): Pending, In Progress, Completed
- deadline (DateTimeField): Optional due date
- priority (ForeignKey): Link to Priority
- category (ForeignKey): Link to Category
- created_at (DateTimeField): Auto timestamp
- updated_at (DateTimeField): Auto timestamp
```

### Priority
```
- name (CharField): Priority name (High, Medium, Low)
- created_at (DateTimeField): Auto timestamp
- updated_at (DateTimeField): Auto timestamp
```

### Category
```
- name (CharField): Category name
- created_at (DateTimeField): Auto timestamp
- updated_at (DateTimeField): Auto timestamp
```

### SubTask
```
- title (CharField): Subtask name
- status (CharField): Same as Task
- task (ForeignKey): Parent Task
- created_at (DateTimeField): Auto timestamp
- updated_at (DateTimeField): Auto timestamp
```

### Note
```
- content (TextField): Note content
- task (ForeignKey): Associated Task
- created_at (DateTimeField): Auto timestamp
- updated_at (DateTimeField): Auto timestamp
```

---

## Troubleshooting

### Issue: "No module named django"
**Solution:** Activate virtual environment and install requirements
```bash
.\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Issue: "No such table: tasks_task"
**Solution:** Run migrations
```bash
python manage.py migrate
python manage.py init_data
```

### Issue: Dropdowns are empty (no priorities/categories)
**Solution:** Initialize default data
```bash
python manage.py init_data
```

### Issue: Server won't start on port 8000
**Solution:** Either:
- Close other apps using port 8000, or
- Run on different port: `python manage.py runserver 8001`

### Issue: Changes not appearing
**Solution:** 
1. Stop the server (Ctrl+C)
2. Restart server: `python manage.py runserver`
3. Hard refresh browser: Ctrl+F5

### Issue: Database locked
**Solution:** 
- Close all open connections
- Remove `db.sqlite3` and run: `python manage.py migrate && python manage.py init_data`

---

## Tips & Best Practices

💡 **Time Management**
- Use High priority for urgent tasks
- Medium for regular tasks, Low for flexible ones
- Set realistic deadlines

📁 **Organization**
- Assign categories to keep tasks organized
- Use descriptions for complex tasks
- Review and update status regularly

⚡ **Productivity**
- Check dashboard daily
- Filter by status to focus on in-progress tasks
- Archive completed tasks by marking them as Completed

🔐 **Admin Tips**
- Create custom categories for your workflow
- Add new priorities if needed
- Regularly backup your database

---

## Support & Contribution

For issues or suggestions:
1. Check the Troubleshooting section
2. Review the code comments
3. Check Django documentation: https://docs.djangoproject.com/

---

**Version:** 1.0  
**Last Updated:** March 15, 2026  
**License:** MIT

Happy task managing! 🚀

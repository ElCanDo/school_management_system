# School Management System API

A Django REST Framework API for managing core school operations, including user onboarding, classroom management, student enrollment, and teacher assignment.

## Overview

This project provides a role-aware backend for a school management workflow. It is designed around a custom user model and a set of academic domain resources exposed through RESTful endpoints.

Most endpoints require authenticated access and are intended for administrative or authorized users.

## Features

- **Role-based user model** for Admin, Teacher, and Student accounts
- **Custom user registration** endpoint
- **Classroom management** with full CRUD support
- **Student management** with enrollment tracking
- **Teacher management** with classroom assignment support
- **JWT authentication** using Simple JWT
- **Browsable API support** for development/testing

## Technology Stack

- **Language:** Python
- **Framework:** Django
- **API Framework:** Django REST Framework
- **Authentication:** djangorestframework-simplejwt (JWT)
- **Database:** MySQL
- **Deployment target:** PythonAnywhere

## Live Deployment

- Base URL: `https://princen.pythonanywhere.com/`

## API Endpoints

### Core Routes

| Endpoint | Description |
|---|---|
| `/api/` | API root |
| `/api/register/` | Register a new user |
| `/api/users/` | List/manage users |
| `/api/classrooms/` | List/manage classrooms |
| `/api/teachers/` | List/manage teachers |
| `/api/students/` | List/manage students |
| `/api/enrollments/` | View/manage student enrollments |
| `/api/teacher-assignments/` | View/manage teacher-classroom assignments |

### Authentication Routes

| Endpoint | Description |
|---|---|
| `/api/register/` | Custom User Registration |
| `/api/token/` | Obtain JWT access and refresh tokens |
| `/api/token/refresh/` | Refresh an access token |

## Data Model (High-Level)

The API is centered around these entities:

- **User**: Base identity model (admin/teacher/student roles)
- **Student**: Student profile and school-specific attributes
- **Teacher**: Teacher profile and specialization details
- **Classroom**: Class definitions and metadata
- **Enrollment**: Student-to-classroom mapping
- **Teacher Assignment**: Teacher-to-classroom mapping

## Getting Started (Local Development)

> Project code lives in the `school_management_system/` directory.

### 1) Clone the repository

```bash
git clone https://github.com/ElCanDo/Capstone_Project.git
cd Capstone_Project/school_management_system
```

### 2) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure MySQL

Update database settings in `school_management_system/settings.py` to match your local MySQL credentials/database name.

### 5) Apply migrations

```bash
python manage.py migrate
```

### 6) Create an admin account

```bash
python manage.py createsuperuser
```

### 7) Run the development server

```bash
python manage.py runserver
```

Access the API at `http://127.0.0.1:8000/`.

## Permissions & Access

- Default API permission is authenticated access.
- JWT authentication is enabled globally in DRF settings.
- Endpoint behavior is role-aware based on the authenticated user.

## Roadmap

Potential next improvements:

- School profile/registry module
- Subject and curriculum management
- Attendance tracking
- Grading and assessment workflows
- More granular role/record-level permissions
- Frontend client integration

## License

This project was developed as an academic capstone for learning and demonstration purposes.

## Author

**Prince Nyarko**  
Backend Developer (Python, Django, REST APIs)

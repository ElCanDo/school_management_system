# School Management System API

## Overview
This is a **School Management System backend** built with **Django** and **Django REST Framework (DRF)**.  
The system allows schools to manage users, students, teachers, classrooms, enrollments, and more. For now, Only Admin can manage and organize students, teachers and classrooms.

This project is a **capstone project** completed in 5 parts:
1. Idea & Planning
2. Design (ERD & API endpoints)
3. Backend Implementation (core modules)
4. Feature Expansion
5. Finalization & Submission

---

## Live Deployment
The project is deployed and accessible at:  
🌐 [https://princen.pythonanywhere.com/](https://princen.pythonanywhere.com/)

---

## Features

### Core Features (MVP)
- User registration & authentication (admin, teacher, student)
- CRUD operations for:
  - Students
  - Teachers
  - Classrooms
  - Subjects
  - Enrollments
  - Teacher Assignment
- Auto-generation of user IDs
- Linking students to classrooms (enrollment)
- Teacher assignments to classrooms(teacher assign)

### Future Enhancements
- Subjects management
- Attendance tracking
- Grading system
- Advanced permissions
- Frontend integration

---

## API Endpoints
Here are some of the main API endpoints:

| Endpoint | Description |
|----------|-------------|
| `/api/` | API root |
| `/api/register/` | Register a new user |
| `/api/users/` | List or manage users |
| `/api/classrooms/` | List or manage classrooms |
| `/api/teachers/` | List or manage teachers |
| `/api/students/` | List or manage students |
| `/api/enrollments/` | View and manage student enrollments |
| `/api/teacher-assignments/` | View and assign teachers to classrooms |

---

## ERD Diagram
The database is structured based on the following core models:
- **User**: Stores all users (admin, teacher, student)
- **Student**: Stores student profiles with parent contact and medical info
- **Teacher**: Stores teacher profiles with subject specialization
- **Classroom**: Stores classrooms with assigned teachers
- **Enrollment**: Links students to classrooms

![ERD Diagram](https://dbdiagram.io/d/School-Management-System-ERD-692b4544d6676488bae8ba7b)

---

#Running Locally
## Installation

#### Step 1. Clone the repository:
```bash
git clone https://github.com/ElCanDo/Capstone_Project.git
cd Capstone_Project
```


#### Step 2. Create a virtual environment:

python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows


#### Step 3. Install dependencies:

pip install -r requirements.txt


#### Step 4. Apply migrations:

python manage.py migrate


#### Step 5. Create a superuser (optional):

python manage.py createsuperuser


#### Step 6. Run the development server:

python manage.py runserver

#### Step 7. Go to https://http://127.0.0.1:8000/

# School Management System API

## Overview
This is a **School Management System backend** built with **Django** and **Django REST Framework (DRF)**.  
The system allows schools to manage users, students, teachers, classrooms, enrollments, and more. Admins can register their school, and teachers can manage their classrooms and students.

This project is a **capstone project** completed in 5 parts:
1. Idea & Planning
2. Design (ERD & API endpoints)
3. Backend Implementation (core modules)
4. Feature Expansion
5. Finalization & Submission

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
- Teacher assignments to classrooms

### Future Enhancements
- Subjects management
- Attendance tracking
- Grading system
- Advanced permissions
- Frontend integration

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

## Installation

#### Step 1. Clone the repository:
```bash
git clone https://github.com/yourusername/school-management-system.git
```
cd school-management-system


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

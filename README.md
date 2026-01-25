# School Management System API

School Management System API 

A RESTful School Management System API built with Django and Django REST Framework (DRF) for managing school operations such as users, students, teachers and classrooms.

Most endpoints require admin authentication. The deployment demonstrates API structure and behavior rather than open public access.

✨ Key Features 
- Role-based user system (Admin, Teacher, Student) 
- Custom user model with auto-generated user IDs
- Student enrollment into classrooms 
- Teacher assignment to classrooms 
- Full CRUD support for core entities 
- RESTful API design using Django REST Framework 

🛠️ Tech Stack Backend:
- Python,
- Django, 
- Django REST Framework 

Database: 
- MySQL

Authentication: 
- Simple JWT Authentication

Deployment: 
- PythonAnywhere 
https://princen.pythonanywhere.com/


Endpoints support standard HTTP methods (GET, POST, PUT, DELETE) based on user permissions.


---

## API Endpoints

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
- **Teacher-Assign**: Links teachers to classrooms

![ERD Diagram](https://dbdiagram.io/d/School-Management-System-ERD-692b4544d6676488bae8ba7b)

---

#Running Locally

⚙️ Running Locally Installation 

1. Clone the repository git clone
https://github.com/ElCanDo/Capstone_Project.git 
cd Capstone_Project 

2. Create and activate a virtual environment 
python -m venv venv 

Linux / macOS
source venv/bin/activate 

Windows
venv\Scripts\activate 

3. Install dependencies:
pip install -r requirements.txt 

4. Apply migrations:
python manage.py migrate

5. Create a superuser:
python manage.py createsuperuser 

6. Run the development server: 
 python manage.py runserver 

Access the API at: http://127.0.0.1:8000/

---

###🔮 Future Improvements:

- School Register (Register the name of aschool)
- Subjects management(Include subject management into the system)
- Attendance tracking (Track student attendance to school)
- Grading and Assessment system (Manage students classrooms tests and examinations)

- Advanced role-based permissions (Teachers being able to manage their class students records and students viewing their records on the system)
- Frontend integration

---


📄 License 

- This project is developed as an academic capstone project for learning and demonstration purposes.

👤 Author 

- Prince Nyarko 
Backend Developer(Python, Django & REST APIs)


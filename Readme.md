# Course Enrollment System

This project provides a Course Enrollment System with REST API endpoints for managing courses and students. Additionally, it includes a frontend interface for student enrollment and viewing enrolled students.

## Setup Instructions (Docker)

### Clone the Repository

git clone https://github.com/Kushaldotel/coursemanagement.git
cd coursemanagement
cd managecourse

### Docker command to follow

- docker-compose up --build
- docker-compose exec web python manage.py createsuperuser (to create a superuser)
- Then navigate to the urls mentioned below in API Endpoints

## Setup Instructions (Local Development)

### Clone the Repository

git clone https://github.com/Kushaldotel/coursemanagement.git
cd coursemanagement
cd managecourse


### Create a Virtual Environment
sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## create a .env file
Make sure to have this in a .env file inside managecourse folder

- DB_NAME='your_db_name'
- DB_USER='Your_user'
- DB_PASSWORD='your_password'
- DB_HOST=localhost # as you are running locally


- EMAIL_HOST_USER='your_email'
- EMAIL_HOST_PASSWORD='your Password'
- DEFAULT_FROM_EMAIL='your email'

### Install Dependencies
pip install -r requirements.txt


### Apply Migrations
python manage.py migrate


### 5️⃣ Create a Superuser (Optional for Admin Access)
python manage.py createsuperuser


### 6️⃣ Run the Development Server
python manage.py runserver


## API Endpoints

- Rest Api can be accessed via:

    http://127.0.0.1:8000//course/categories/ (categories of courses)

    http://127.0.0.1:8000//course/courses/ (courses api with content)

    http://127.0.0.1:8000//course/mcqs/ (mcqs api)

    http://127.0.0.1:8000//course/mcqs/<int:course_id>/ (To get all the mcqs for a course)

    http://127.0.0.1:8000//course/enrollments/ (Api to get all the enrolled student in different courses)


- Frontend Page can be accessed via:

    http://127.0.0.1:8000/admin/ (To access admin page)

    make sure you are loggedin as an admin before accessing below 2 APIs.

    http://127.0.0.1:8000/account/create-student-page/ (To create student)

    http://127.0.0.1:8000//course/enrollment-page/ (To see total enrolled student list)




## Tech Stack
- Backend: Django, Django REST Framework
- Frontend: HTML, CSS, JavaScript (Fetch API)
- Database: PostgreSQL
- Admin: django-unfold

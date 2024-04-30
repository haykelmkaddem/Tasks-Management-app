# Task Management Django Project

Welcome to the Task Management Django project! This project is designed to help you manage tasks efficiently.

## Getting Started

### 1. Clone the Project and Environment Configuration

To get started, clone the project repository to your local machine:

```bash
git clone <repository-url>


Next, navigate into the project directory

Create and activate a virtual environment:

# On Unix or MacOS
python3 -m venv env
source env/bin/activate

# On Windows
python -m venv env
.\env\Scripts\activate


Install the project dependencies:
pip install -r requirements.txt

Setting Up PostgreSQL:
Before running the application, you need to install PostgreSQL and create a database for the project.
Download and install PostgreSQL from the official website
After installing PostgreSQL, open a terminal and log in to PostgreSQL as a superuser:
psql -U postgres

Create a new database for the project
CREATE DATABASE task_management_db;

Configure .env File
Copy the .env.example file to .env:
cp .env.example .env


Before running the application, ensure that Redis is installed and running on your system.
Start Redis server:
redis-server

Celery is used for asynchronous task execution in this project. To start Celery, run the following command from the project root directory:
celery -A task_management_project worker --loglevel=info


To run the Django project, navigate to the project directory and run the following command:
python manage.py runserver

By default, the application will be available at: http://localhost:8000


To run tests for the application, execute the following command from the project root directory:

python manage.py test tasks.tests.test_models
python manage.py test tasks.tests.test_services
python manage.py test tasks.tests.test_views

To test the admin Interface execute this command to create a new superuser :
python manage.py createsuperuser

put the username and the password
and now you can use the admin interface with this link :
http://localhost:8000/admin/

# To-Do List Application

## Introduction
This is a full-stack web application for managing tasks in a To-Do list. It allows users to create, read, update, and delete (CRUD) tasks. The backend is built using Django and Django REST Framework to provide a REST API, and the frontend is implemented with HTML, CSS, and JavaScript.

## Project Structure
ToDoList/ ├── crud/ │ ├── models.py │ ├── serializers.py │ ├── views.py │ ├── urls.py ├── static/ │ ├── css/ │ ├── js/ ├── templates/ │ ├── index.html ├── ToDoList/ │ ├── settings.py │ ├── urls.py └── manage.py


## Features
- **CRUD operations**: Add, view, edit, and delete tasks.
- **Switch between table and card views**: Users can choose how they want to display tasks for better visibility.
- **RESTful API**: Utilizes Django REST Framework to expose the backend API.
- **Responsive UI**: The frontend adapts to various screen sizes, including mobile devices.
- **Enhanced UI/UX**: Includes hover effects and intuitive form layouts tailored for ease of use.
- **Preloader**: An animated preloader for better user experience while the content loads.
- **CSRF protection**: Security layer implemented in all forms and API requests.

## Core Work and Challenges
- **Backend Development with Django REST Framework**: One of the core challenges was setting up and connecting the Django backend with the frontend to ensure that the data flowed seamlessly between them. Designing the API and handling complex request-response cycles while maintaining data integrity was key to this project.
  
- **Handling CRUD Operations**: Implementing create, read, update, and delete (CRUD) operations on the frontend with real-time interaction from the backend was tricky. Coordinating the Django models and serializers with JavaScript's fetch API for dynamic updates was challenging but rewarding.

- **Dynamic Data Fetching with JavaScript**: Another challenge was fetching data from the backend and rendering it dynamically on the frontend using JavaScript's promises and `fetch()`. The handling of asynchronous data and integrating it into the UI required careful management of the frontend-backend interaction, especially with the new table and card view options.

- **Cross-Site Request Forgery (CSRF) Protection**: Managing CSRF tokens when performing API requests from JavaScript was a challenge. It required careful setup to ensure secure data transactions while maintaining a seamless user experience.

- **Responsive Design**: Ensuring the design worked smoothly across all devices, especially for forms and tables, involved troubleshooting CSS for responsiveness, including media queries and adjusting layouts for mobile devices.

## API Endpoints
- **GET /api/items/**: Retrieve all tasks
- **POST /api/items/**: Add a new task
- **GET /api/items/{id}/**: Retrieve a specific task
- **PUT /api/items/{id}/**: Update a task
- **DELETE /api/items/{id}/**: Delete a task

## Installation & Setup
### Prerequisites
- Python 3.8+
- Django 4.x
- Django REST Framework

### Setup Instructions
**Note:** After creating the virtual environment, please place this repository folder within the virtual environment folder. It is advisable to name the virtual environment folder "env," as I have done, to minimize the need for extensive edits.Additionally you have to run a command 'python manage.py collectstatic' in the terminal.
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todo-list.git
    cd todo-list
    ```
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the server:
    ```bash
    python manage.py runserver
    ```
6. Access the application at `http://127.0.0.1:8000/`


# CodeAlpha Backend Development Internship

This repository contains my projects completed during the **CodeAlpha Backend Development Internship**. The projects focus on Python backend development, REST APIs, database operations, and API testing.

## 🚀 Projects

### Task 1: URL Shortener

A Flask-based backend application that converts long URLs into short URLs and redirects users to the original URLs.

**Technologies Used**
- Python
- Flask
- SQLite
- REST API
- Git and GitHub
- Postman

**Features**
- Shorten long URLs
- Generate unique short codes
- Store URLs in an SQLite database
- Redirect short URLs to their original destinations
- Provide a health-check endpoint
- Handle missing URLs and unknown short codes

**Project Folder:** `Task_1_URL_Shortener`

### Task 2: Event Registration System

A Django REST Framework application for managing events and user registrations.

**Technologies Used**
- Python
- Django
- Django REST Framework
- SQLite
- REST API
- Git and GitHub
- Postman

**Features**
- Create and list events
- Retrieve event details
- Register users for events
- Prevent duplicate registrations
- Check event capacity before registration
- View event registrations
- Cancel registrations
- Handle invalid requests and missing records

**Project Folder:** `Task_2_Event_Registration_System`

## 📂 Repository Structure

```text
CodeAlpha_Backend_Development_Internship/
│
├── Task_1_URL_Shortener/
│   ├── app.py
│   ├── README.md
│   └── requirements.txt
│
├── Task_2_Event_Registration_System/
│   ├── manage.py
│   ├── event_registration/
│   ├── events/
│   ├── README.md
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

## ⚙️ How to Run the Projects

### Task 1: URL Shortener

1. Open the Task 1 folder.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Test the API using Postman.

### Task 2: Event Registration System

1. Open the Task 2 folder.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Test the API endpoints using Postman.

## 🧪 API Testing

The API endpoints were tested using Postman to check successful requests, validation errors, duplicate registrations, event capacity, and registration cancellation.

Refer to each project's README file for its API endpoints, example requests, and setup instructions.

## 🎯 Skills Demonstrated

- Python backend development
- Flask application development
- Django REST Framework
- REST API design and implementation
- SQLite database operations
- Request validation and error handling
- API testing with Postman
- Git and GitHub version control
- Project documentation

## 👨‍💻 About

This repository documents my practical learning and project work during the CodeAlpha Backend Development Internship.

**GitHub:** https://github.com/dinushan02/CodeAlpha_Backend_Development_Internship

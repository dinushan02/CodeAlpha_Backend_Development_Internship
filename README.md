# 🚀 CodeAlpha Backend Development Internship

A collection of backend development projects built using **Python** as part of my **CodeAlpha Backend Development Internship**.

This repository documents my hands-on learning journey in backend development, REST APIs, databases, server-side programming, and application business logic.

## 🎯 Internship Objective

The objective of this internship is to gain practical experience in backend development by building real-world applications and implementing core backend concepts.

Throughout this internship, I am focusing on:

- Python backend development
- RESTful API design
- Backend architecture
- Database design and integration
- CRUD operations
- API request and response handling
- Input validation and error handling
- Database relationships
- Backend business logic
- Git and GitHub
- Project documentation and testing

## 🛠️ Technologies and Tools

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Frameworks | Flask, Django |
| API Development | Django REST Framework, REST APIs, JSON |
| Database | SQLite |
| Development Tools | VS Code, Git, GitHub |
| API Testing | Postman, Django REST Framework Browsable API |

Additional technologies may be introduced as the projects evolve.

## 📂 Projects

This repository is organized around three backend development projects selected for my internship portfolio.

### 1. Simple URL Shortener

**Folder:** `Task_1_URL_Shortener`

A backend application that converts long URLs into short URLs using a generated short code.

**Implemented functionality**

- Accept long URLs through an API
- Generate short codes
- Store URL mappings in SQLite
- Redirect short URLs to their original destinations

**Technologies**

- Python
- Flask
- SQLite
- REST API

**Key concepts**

- Flask application structure
- HTTP methods and API endpoints
- JSON request and response handling
- Database integration
- URL routing and redirects
- Short-code generation

### 2. Event Registration System

**Folder:** `Task_2_Event_Registration_System`

A backend application for managing events and user registrations using Django and Django REST Framework.

**Implemented functionality**

- Retrieve event lists and individual event details
- Create events
- Register users for events
- Prevent duplicate registrations
- Check event capacity before registration
- View registrations for an event
- Cancel registrations

**Technologies**

- Python
- Django
- Django REST Framework
- SQLite
- Postman

**Key concepts**

- Django project structure
- Models and serializers
- Database relationships
- REST API development
- CRUD operations
- Input validation
- HTTP status codes
- Registration business logic

### 3. Job Board Platform

**Folder:** `Task_4_Job_Board_Platform`

A planned backend application for managing job listings, employers, candidates, and job applications.

**Planned functionality**

- Create and manage job listings
- Search and filter jobs
- Manage employer and candidate information
- Apply for jobs
- Track application statuses
- Implement application validation and business rules

Resume uploads, authentication, and other advanced features may be added as development progresses.

**Planned technologies**

- Python
- Django
- Django REST Framework
- SQLite

**Key concepts to explore**

- Complex database relationships
- RESTful API design
- Search and filtering
- Application workflows
- Status management
- File uploads, if implemented
- Authentication and authorization, if implemented

## 🧠 Skills and Concepts

The projects help me develop practical experience with:

```text
Python
   ↓
Backend Development
   ↓
Flask and Django
   ↓
REST APIs
   ↓
HTTP and JSON
   ↓
Database Integration
   ↓
CRUD Operations
   ↓
Validation and Error Handling
   ↓
Backend Business Logic
   ↓
Git and GitHub
```

## 📈 Learning Progression

The projects follow a progression from fundamental backend concepts to more complex application workflows.

```text
Project 1 — URL Shortener
API Fundamentals → Routing → SQLite → Redirects
   ↓
Project 2 — Event Registration System
Django → Models → Serializers → Relationships → Registrations
   ↓
Project 3 — Job Board Platform
Job Listings → Search → Applications → Status Management
```

## 📁 Repository Structure

```text
CodeAlpha_Backend_Development_Internship/
│
├── README.md
│
├── Task_1_URL_Shortener/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   └── ...
│
├── Task_2_Event_Registration_System/
│   ├── manage.py
│   ├── requirements.txt
│   ├── README.md
│   └── ...
│
└── Task_4_Job_Board_Platform/
    ├── manage.py
    ├── requirements.txt
    ├── README.md
    └── ...
```

*Note: The Job Board Platform folder will be added when development begins. Individual project structures may vary.*

## 💻 How to Run the Projects

Each project has its own dependencies and setup instructions.

### Example: Run the URL Shortener

From the repository root:

```bash
cd Task_1_URL_Shortener
python -m venv venv
```

Activate the virtual environment.

**Windows — Command Prompt**

```bat
venv\Scripts\activate
```

**Windows — Git Bash**

```bash
source venv/Scripts/activate
```

**macOS or Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Follow the project's `README.md` for database setup and instructions to start the application.

### Run the Event Registration System

From the repository root:

```bash
cd Task_2_Event_Registration_System
python -m venv venv
```

Activate the environment, then run:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open the API in your browser:

http://127.0.0.1:8000/api/events/

Refer to the individual README files for complete setup instructions.

## 🧪 Testing

Testing is performed using the tools appropriate to each project, including Postman and Django REST Framework's browsable API.

Tests cover relevant API operations, request validation, successful responses, and error handling.

## 📚 Project Documentation

Each project has its own README containing relevant information about:

- Project overview
- Features
- Technologies used
- Installation and setup
- API endpoints
- Example requests and responses
- Testing information
- Project status

## 🎓 Internship Information

- **Organization:** CodeAlpha
- **Domain:** Backend Development
- **Programming Language:** Python

This repository documents my practical work and learning progress during the CodeAlpha Backend Development Internship.

## 👨‍💻 About Me

I am an aspiring Python Developer focused on strengthening my programming, problem-solving, and backend development skills through practical projects.

I am continuously improving my knowledge of:

- Python
- Backend Development
- REST APIs
- Databases
- Django and Flask
- Data Structures and Algorithms
- Software Development

## 🔗 Portfolio

- **GitHub:** [dinushan02](https://github.com/dinushan02)
- **YouTube:** [@CodewithDinushan](https://www.youtube.com/@CodewithDinushan)

## ⭐ Explore the Projects

Feel free to explore the source code, review the project documentation, and follow my backend development journey.

**Built with Python 🐍 | Learning by Building 🚀**
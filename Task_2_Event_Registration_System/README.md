# Event Registration System

A backend application developed using Django and Django REST Framework as part of my CodeAlpha Backend Development Internship.

The project provides REST API endpoints for creating events, retrieving event information, registering users for events, viewing registrations, and cancelling registrations.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Git and GitHub
- Postman

## Features

- Create new events
- Retrieve a list of events
- Retrieve event details by ID
- Register users for events
- Prevent duplicate registrations
- Check event capacity before registration
- View registrations for a specific event
- Cancel an existing registration
- Return appropriate HTTP status codes for successful requests and errors

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/events/` | Retrieve all events |
| POST | `/api/events/` | Create a new event |
| GET | `/api/events/<id>/` | Retrieve details of a specific event |
| GET | `/api/events/<id>/register/` | View registrations for an event |
| POST | `/api/events/<id>/register/` | Register a user for an event |
| DELETE | `/api/events/<id>/register/` | Cancel a user's registration |

Replace `<id>` with the relevant event ID.

## Example: Create an Event

**Request**

`POST /api/events/`

**JSON body**

```json
{
  "title": "Django Backend Workshop",
  "description": "Learn to build REST APIs using Django",
  "date": "2026-12-15T10:00:00Z",
  "location": "Colombo",
  "capacity": 50
}
```

## Example: Register a User

**Request**

`POST /api/events/1/register/`

**JSON body**

```json
{
  "user_id": 1
}
```

The user must exist in the database. Registration is rejected if the user is already registered or the event has reached its capacity.

## Example: Cancel a Registration

**Request**

`DELETE /api/events/1/register/`

**JSON body**

```json
{
  "user_id": 1
}
```

The API returns a success message when the registration is cancelled. If the registration does not exist, it returns a `404 Not Found` response.

## How to Run the Project

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Create and activate a Python virtual environment.
4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open the API in your browser:

   `http://127.0.0.1:8000/api/events/`

## Testing

The API was tested using Django REST Framework's browsable API and Postman.

Tests performed include:

- Retrieving events and event details
- Creating an event
- Registering a user
- Preventing duplicate registrations
- Viewing event registrations
- Cancelling a registration
- Confirming that cancelling an already-cancelled registration returns `404 Not Found`

## Project Status

Completed core event management and registration API functionality, with testing performed for the documented endpoints.

## Internship

Developed as part of the CodeAlpha Backend Development Internship.

## Author

Dinushan
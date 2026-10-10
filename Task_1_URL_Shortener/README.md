# 🔗 URL Shortener Backend

A simple URL Shortener Backend built with **Python**, **Flask**, and **SQLite**. This project provides a REST API to generate short URLs, store URL mappings in a database, and redirect users to their original URLs.

## ✨ Features

- Flask backend application
- Home endpoint to check whether the server is running
- Health-check API returning a JSON response
- REST API endpoint to receive long URLs
- Random short-code generation using Python's `secrets` module
- Short-code uniqueness checking
- SQLite database for storing original URLs and their short codes
- Redirect short URLs to their original destinations
- JSON responses for successful requests and errors
- Basic input validation for missing URLs
- HTTP status codes for successful requests and errors

## 🛠️ Technologies Used

- **Python 3**
- **Flask** — backend web framework
- **SQLite** — database
- **SQL** — database queries
- **Postman** — API testing
- **Git & GitHub** — version control and source code management

## 📁 Project Structure

```text
Task_1_URL_Shortener/
├── app.py
├── README.md
├── requirements.txt
├── url_shortener.db  # Created automatically when the database is initialized
└── venv/             # Local virtual environment; not committed to Git
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3 installed
- Git installed (optional, for version control)

### 1. Clone the repository

If you are cloning the main internship repository, run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then navigate to the project folder:

```bash
cd CodeAlpha_Backend_Development_Internship/Task_1_URL_Shortener
```

If you have already downloaded or opened the project, navigate directly to `Task_1_URL_Shortener`.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows — Command Prompt:**

```bash
venv\Scripts\activate
```

**Windows — Git Bash:**

```bash
source venv/Scripts/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the application

```bash
python app.py
```

The Flask development server usually runs at:

```text
http://127.0.0.1:5000
```

The SQLite database and its `urls` table are initialized when the application starts.

> **Note:** Flask's built-in development server is intended for local development, not production deployment.

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks whether the backend is running |
| GET | `/api/health` | Returns the backend health status |
| POST | `/api/shorten` | Generates a short code and stores the URL mapping |
| GET | `/<short_code>` | Redirects to the original URL associated with the short code |

## 🧪 API Usage and Examples

### 1. Home Endpoint

**Request**

```http
GET /
```

**Expected response**

```text
URL Shortener Backend is Running!
```

### 2. Health-Check Endpoint

**Request**

```http
GET /api/health
```

**Example response**

```json
{
  "status": "success",
  "message": "Backend is healthy"
}
```

### 3. Create a Short URL

**Request**

```http
POST /api/shorten
```

**Content-Type**

```text
application/json
```

**Request body**

```json
{
  "url": "https://www.python.org/"
}
```

**Example response**

```json
{
  "status": "success",
  "original_url": "https://www.python.org/",
  "short_code": "1a3c9c",
  "short_url": "http://127.0.0.1:5000/1a3c9c"
}
```

> The short code in this example is illustrative. Your application generates a random code, so your response may differ.

### 4. Redirect to the Original URL

After creating a short URL, open the returned `short_url` in your browser.

For example:

```text
http://127.0.0.1:5000/1a3c9c
```

The backend looks up the short code in SQLite and redirects the browser to the corresponding original URL.

A successful redirect typically returns HTTP `302 Found`.

### 5. Handle Missing URLs

If the request body does not contain a URL, the API returns HTTP `400 Bad Request`.

**Example request body**

```json
{}
```

**Example response**

```json
{
  "status": "error",
  "message": "URL is required"
}
```

### 6. Handle Unknown Short Codes

If a requested short code does not exist in the database, the backend returns HTTP `404 Not Found`.

**Example response**

```json
{
  "status": "error",
  "message": "Short URL not found"
}
```

## 🗄️ Database Design

The application uses SQLite to store URL mappings in a table named `urls`.

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Auto-incrementing primary key |
| `short_code` | TEXT | Unique code associated with the original URL |
| `original_url` | TEXT | Original destination URL |

The `short_code` column has a `UNIQUE` constraint to prevent duplicate codes from being stored.

The application checks whether a generated code already exists before saving the URL mapping.

## 🔄 How It Works

1. A client sends a long URL to `POST /api/shorten`.
2. The backend checks that a URL was provided.
3. Python generates a random short code.
4. The backend checks whether the generated code already exists.
5. The short code and original URL are saved in SQLite.
6. The API returns the original URL, short code, and generated short URL.
7. When a user visits the short URL, Flask retrieves the original URL from SQLite.
8. Flask redirects the user to the original destination.

## 🧪 Testing

You can test the API using **Postman**.

Keep the Flask server running while testing.

1. Test `GET /` to check the server response.
2. Test `GET /api/health` to check the health endpoint.
3. Send a JSON request to `POST /api/shorten`.
4. Open the returned short URL in your browser.
5. Send an empty JSON object `{}` to test missing-URL validation.
6. Visit an unknown short code to test the `404` response.

## 🔒 Current Limitations

- URL validation currently checks for a missing URL but does not fully validate URL format.
- Short codes are randomly generated; the uniqueness check helps prevent collisions.
- The generated short URLs use a local development address and are not publicly accessible.
- The application has not yet been configured for production deployment.
- No user authentication or URL-management interface is currently implemented.

## 🚀 Future Improvements

- Stronger URL validation
- Improved database error handling
- Better handling of database connection failures
- Configurable base URL for deployment
- Automated tests for API endpoints
- Deployment to a hosting platform
- Optional frontend interface for creating and managing short URLs

## 🎯 Project Objective

The goal of this project is to develop practical backend development skills by building a URL Shortener API with Flask and SQLite. It demonstrates REST API design, HTTP methods and status codes, database operations, short-code generation, and URL redirection.

---

**Built with Python and Flask as part of the CodeAlpha Backend Development Internship.**